from django.shortcuts import render, redirect
from .models import Clothing
from .forms import ClothingForm
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from django.contrib.auth.decorators import login_required
from fabrik.settings import LOGIN_REDIRECT_URL
from .tagsToTags import tagsToTags
from django.db import IntegrityError

#Jason's Clarifai Client ID, Client Secret

app =  ClarifaiApp("wPXX8nSrRj_A25bqQAdAurGdZdbxzhJWELL9aaQ2","SRRlIyrXfV7bJkNE7R3naCBPkxw3J-UwqVgcxJhJ")
#Model for Apparel Prediction
#model = app.models.get('e0be3b9d6a454f0493ac3a30784001ff')

#Takes a URL in text, returns the response as a string
#This function is the main part of this code, use it to format any clarifai API response
def clarify(url):
    x = app.tag_urls(urls=[url], model='e0be3b9d6a454f0493ac3a30784001ff')
    clothing_type = x['outputs'][0]['data']['concepts'][0]['name']
    return clothing_type

#Categorizes a clothing tag to an appropriate weather season.
# Create your views here.

@login_required(login_url=LOGIN_REDIRECT_URL)
def index(request):
    closet = Clothing.objects.filter(owned_by=request.user)
    return render(request, 'clothes/index.html', {'closet' : closet})

@login_required(login_url=LOGIN_REDIRECT_URL)
def add(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            image = data['image']
            x = Clothing.objects.create(
                name = name,
                image = image,
                owned_by = request.user
                )
            try:
                x.clothing_type = tagsToTags(clarify(x.image.url), 1)
                x.clothing_location = tagsToTags(clarify(x.image.url), 0)
                x.save()
                form.save()
                return redirect('/')
            except IntegrityError:
                return redirect('/')

    else:
        form = ClothingForm()
    return render(request, 'clothes/add.html', {'form' : form})