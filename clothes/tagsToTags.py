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
            'snow' : set(['Gloves', 'Women\'s Boots', 'Peacoat', 'Men\'s Hat', 
                            'Men\'s Boots', 'Overalls']),
            'chilly' : set(['Blazer', 'Leather Jacket', 'Bomber Jacket',
                            'Cardigan', 'Men\'s Dress Shoes', 'Tights', 
                            'Relaxed Pants', 'Denim Jacket', 'Platform Shoes',
                            'Vest', 'Tracksuit', 'Oxfords', 'Loafers', 
                            'Boatshoes', 'Polos']),
            'sunny' : set(['Capris', 'Cocktail Dress', 'T-Shirt', 'Kimonos', 
                            'Pumps', 'Robe', 'Women\'s Sandals', 
                            'Spring Jacket', 'Men\'s Sandals']),
            'cold' : set(['Sneakers', 'Puffy Coat', 'Fleece Jacket', 
                            'Button Down', 'Skinny Pants', 'Sweatshirt', 
                            'Women\'s Hat', 'Wide Leg Pants', 'Hoodies']),
            'rain' : set(['Raincoats', 'Umbrella']),
            'any' : set(['Socks', 'Wristlet & Clutch'])
        }
        #else:
            #return 'ERROR: No Such Clothing Object in database.'
        
        # Checks the kind of weather the garment can be worn in
        for weather, name in condition.items():
            if tag in name:
                return weather
    else:
        return 'Bad Flag Value'