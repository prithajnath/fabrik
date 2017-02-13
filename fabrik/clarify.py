#Takes a url as input from the command line,
#and creates a file with the clarifai output

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
    x = ClImage(url = urlstr)
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

imageurl = str(input("Input a url:"))
print(clarify(imageurl))
