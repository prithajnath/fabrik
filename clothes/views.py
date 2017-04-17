from django.shortcuts import render, redirect
from .models import Clothing
from .forms import ClothingForm
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from django.contrib.auth.decorators import login_required
from fabrik.settings import LOGIN_REDIRECT_URL
import base64
#Jason's Clarifai Client ID, Client Secret
app =  ClarifaiApp("wPXX8nSrRj_A25bqQAdAurGdZdbxzhJWELL9aaQ2","SRRlIyrXfV7bJkNE7R3naCBPkxw3J-UwqVgcxJhJ")
#Model for Apparel Prediction
model = app.models.get('e0be3b9d6a454f0493ac3a30784001ff')

#Takes a URL in text, returns the response as a string
#This function is the main part of this code, use it to format any clarifai API response
def clarify(file):
    b64 = base64.encode(file)
    x = app.inputs.create_image_from_base64(b64)

    predictions = str(model.predict([x]))

    #Outputing the response string to a file and formatting it
    fil = open('output.txt', 'w')
    for i in predictions:
        if i == '}':
            fil.write('}\n')
        else:
            fil.write(i)

    #Takes the highest confidence line
    fil = open('output.txt','r')
    for line in fil:
        if (('\'id\': \'ai' in line) == True):
            result = line
            print(line)
            break

    #Takes only the name
    result1 = result[(result.find('\'name\':')+7):]
    result2 = result1[:result1.find(',')]
    return result2

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
            clothing_type = data['clothing_type']
            image = data['image']
            x = Clothing.objects.create(
                name = name,
                image = image,
                clothing_type = clarify(image),
                owned_by = request.user
                #fWeather = tagsToTags(clothing_type,1)
                #fTags = tagsToTags(clothing_type,0)
                )
            form.save()
            return redirect('/')
    else:
        form = ClothingForm()
    return render(request, 'clothes/add.html', {'form' : form})
