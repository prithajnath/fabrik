#Takes a url as input fromt he command line, and creates a file with the clarifai output

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
#Jason's Clarifai Client ID, Client Secret
app =  ClarifaiApp("wPXX8nSrRj_A25bqQAdAurGdZdbxzhJWELL9aaQ2","SRRlIyrXfV7bJkNE7R3naCBPkxw3J-UwqVgcxJhJ")
#Model for Apparel Prediction
model = app.models.get('e0be3b9d6a454f0493ac3a30784001ff')

#Takes a URL in text, outputs the response as a string
imageurl = str(input("Input a url:"))
x = ClImage(url = imageurl)
predictions = str(model.predict([x]))
print(predictions)

#Outputing the response string to a file and formatting it
fil = open('output.txt', 'w')
for i in predictions:
    if i == '}':
        fil.write('}\n')
    else:
        fil.write(i)
