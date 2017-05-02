from django.shortcuts import render, redirect
from .models import Clothing
from .forms import ClothingForm
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from django.contrib.auth.decorators import login_required
from fabrik.settings import LOGIN_REDIRECT_URL
from .tagsToTags import tagsToTags

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
    #x = app.inputs.create_image_from_filename(urlstr)
    #names = {}
    #for i in model.predict([x])['outputs'][0]['data']['concepts']:
    #    names[i['value']]=i['name']
    #return names[max(names)]

#Categorizes a clothing tag to an appropriate weather season.

<<<<<<< HEAD
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

=======
def tagsBySeason(name):
    if tagsToTags(name, 1) == 'snow':
        return 'winter'
    elif tagsToTags(name, 1) == 'chilly':
        return 'fall'
    elif tagsToTags(name, 1) == 'sunny':
        return 'summer'
    elif tagsToTags(name, 1) == 'cold':
        return 'winter'
    elif tagsToTags(name, 1) == 'rain':
        return 'spring'
    #elif tagsToTags(name, 1) == 'any':
        
    else:
        return 'N/A'
    
>>>>>>> 15195c87dcb4bd865f567f319b1da2c61ef5813b
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
            #clothing_type = data['clothing_type']
            image = data['image']
            #tag = clarify(form.fields['image'].name)
            #form['clothing_type']=tag
            x = Clothing.objects.create(
                name = name,
                #clothing_type = clothing_type,
                image = image,
                owned_by = request.user
                )
            x.clothing_type = tagsBySeason(clarify(x.image.url))
            x.save()
            form.save()
            return redirect('/')
    else:
        form = ClothingForm()
    return render(request, 'clothes/add.html', {'form' : form})