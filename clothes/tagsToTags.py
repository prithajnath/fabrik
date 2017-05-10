''' This function is used to categorize clothing tags based on either where on the
    body the clothing image can be worn, or the weather contitions the clothing
    would most likely be worn in, depending on which flag value is specified
    (0 for body part, 1 for weather conditions). '''


def tagsToTags(tag,flag):
    if(flag == 0):
        part = {
            'hands' : set(['Gloves']),
            'feet' : set(['Women\'s Boots', 'Sneakers', 'Pumps',
                            'Men\'s Dress Shoes', 'Men\'s Boots', 'Socks',
                            'Women\'s Sandals', 'Platform Shoes',
                            'Oxfords', 'Men\'s Sandals', 'Loafers',
                            'Boat Shoes']),
            'torso' : set(['Blazer', 'Leather Jacket', 'Peacoat',
                            'Puffy Coat', 'Bomber Jacket', 'Cocktail Dress', 
                            'T-Shirt', 'Fleece Jacket', 'Kimonos',
                            'Cardigan', 'Button-Down', 'Robe',
                            'Sweatshirt', 'Raincoats', 'Polos',
                            'Denim Jacket', 'Hoodies', 'Vest',
                            'Spring Jacket', 'Wristlet & Clutch', 'Tracksuit'
                            ]),
            'pants' : set(['Capris', 'Skinng Pants', 'Tights',
                            'Wide Leg Pants', 'Relaxed Pants', 'Overalls']),
            'head' : set(['Men\'s Hat', 'Women\'s Hat']),
            'extra' : set(['Umbrella'])
        }
        # Checks to see what body part the clothing type belongs to
        for location, name in part.items():
            if tag in name:
                return location
                
    elif(flag == 1):
    #Weather conditions functional tags
        condition = {
            'Snow' : set(['Gloves', 'Women\'s Boots', 'Peacoat', 'Men\'s Hat', 
                            'Men\'s Boots', 'Overalls']),
            'Clouds' : set(['Blazer', 'Leather Jacket', 'Bomber Jacket',
                            'Cardigan', 'Men\'s Dress Shoes', 'Tights', 
                            'Relaxed Pants', 'Denim Jacket', 'Platform Shoes',
                            'Vest', 'Tracksuit', 'Oxfords', 'Loafers', 
                            'Boatshoes', 'Polos']),
            'Clear' : set(['Capris', 'Cocktail Dress', 'T-Shirt', 'Kimonos', 
                            'Pumps', 'Robe', 'Women\'s Sandals', 
                            'Spring Jacket', 'Men\'s Sandals', 'Socks', 'Wristlet & Clutch']),
            'Mist' : set(['Sneakers', 'Puffy Coat', 'Fleece Jacket', 
                            'Button Down', 'Skinny Pants', 'Sweatshirt', 
                            'Women\'s Hat', 'Wide Leg Pants', 'Hoodies']),
            'Rain' : set(['Raincoats', 'Umbrella']),
        }
        #else:
            #return 'ERROR: No Such Clothing Object in database.'
        
        # Checks the kind of weather the garment can be worn in
        for weather, name in condition.items():
            if tag in name:
                return weather
    else:
        return 'Bad Flag Value'