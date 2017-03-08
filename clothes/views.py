from django.shortcuts import render, redirect
from .models import Clothing
from .forms import ClothingForm
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
#Jason's Clarifai Client ID, Client Secret
app =  ClarifaiApp("wPXX8nSrRj_A25bqQAdAurGdZdbxzhJWELL9aaQ2","SRRlIyrXfV7bJkNE7R3naCBPkxw3J-UwqVgcxJhJ")
#Model for Apparel Prediction
model = app.models.get('e0be3b9d6a454f0493ac3a30784001ff')

#Takes a URL in text, returns the response as a string
#This function is the main part of this code, use it to format any clarifai API response
def clarify(urlstr):
    x = app.inputs.create_image_from_filename(urlstr)
    names = []
    for i in model.predict([x])['outputs'][0]['data']['concepts']:
        names.append(i['name'])
    return names
# Create your views here.

def index(request):
    closet = Clothing.objects.all()
    return render(request, 'clothes/index.html', {'closet' : closet})

def add(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            tag = clarify(form.fields['image'].name)
            form['clothing_type']=tag
            form.save()
            return redirect('index')
    else:
        form = ClothingForm()
    return render(request, 'clothes/add.html', {'form' : form})
