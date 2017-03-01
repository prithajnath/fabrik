#Model for Apparel Prediction
model = app.models.get('e0be3b9d6a454f0493ac3a30784001ff')

#Takes a URL in text, returns the response as a string
#This function is the main part of this code, use it to format any clarifai API response
def clarify(urlstr):
    x = app.inputs.create_image_from_filename(urlstr)
    
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
# Create your models here.
class Clothing(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothes/')
    clothing_type = clarify(Clothing.image.name)

    def __str__(self):
        return self.name

