from clarifai.rest import ClarifaiApp

app =  ClarifaiApp("wPXX8nSrRj_A25bqQAdAurGdZdbxzhJWELL9aaQ2","SRRlIyrXfV7bJkNE7R3naCBPkxw3J-UwqVgcxJhJ")
#Model for Apparel Prediction
#model = app.models.get('e0be3b9d6a454f0493ac3a30784001ff')

x = app.tag_urls(urls=['https://se2fabrik.s3.amazonaws.com/clothes/flannel_s4Fl9c4.jpg?Expires=1493760318&Signature=Mh3j3tESizGCd95LBeP4dNlXHbQ%3D&AWSAccessKeyId=AKIAIZX6HHX5GMQURDCA'],
model='e0be3b9d6a454f0493ac3a30784001ff')
print(x['outputs'][0]['data']['concepts'][0]['name'])