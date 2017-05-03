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
        if(tag == 'Gloves'):
            return 'snow'
        if(tag == 'Women\'s Boots'):
            return 'snow'
        if(tag == 'Blazer'):
            return 'chilly'
        if(tag == 'Capris'):
            return 'sunny'
        if(tag == 'Leather Jacket'):
            return 'chilly'
        if(tag == 'Peacoat'):
            return 'snow'
        if(tag == 'Sneakers'):
            return 'cold'
        if(tag == 'Puffy Coat'):
            return 'cold'
        if(tag == 'Men\'s Hat'):
            return 'snow'
        if(tag == 'Bomber Jacket'):
            return 'chilly'
        if(tag == 'Cocktail Dress'):
            return 'sunny'
        if(tag == 'T-Shirt'):
            return 'sunny'
        if(tag == 'Fleece Jacket'):
            return 'cold'
        if(tag == 'Kimonos'):
            return 'sunny'
        if(tag == 'Pumps'):
            return 'sunny'
        if(tag == 'Cardigan'):
            return 'chilly'
        if(tag == 'Men\'s Dress Shoes'):
            return 'chilly'
        if(tag == 'Men\'s Boots'):
            return 'snow'
        if(tag == 'Button-Down'):
            return 'cold'
        if(tag == 'Robe'):
            return 'sunny'
        if(tag == 'Skinny Pants'):
            return 'cold'
        if(tag == 'Sweatshirt'):
            return 'cold'
        if(tag == 'Tights'):
            return 'chilly'
        if(tag == 'Raincoats'):
            return 'rain'
        if(tag == 'Women\'s Hat'):
            return 'cold'
        if(tag == 'Wide Leg Pants'):
            return 'cold'
        if(tag == 'Polos'):
            return 'chilly'
        if(tag == 'Relaxed Pants'):
            return 'chilly'
        if(tag == 'Denim Jacket'):
            return 'chilly'
        if(tag == 'Socks'):
            return 'any'
        if(tag == 'Hoodies'):
            return 'cold'
        if(tag == 'Women\'s Sandals'):
            return 'sunny'
        if(tag == 'Platform Shoes'):
            return 'chilly'
        if(tag == 'Vest'):
            return 'chilly'
        if(tag == 'Spring Jacket'):
            return 'sunny'
        if(tag == 'Wristlet & Clutch'):
            return 'any'
        if(tag == 'Tracksuit'):
            return 'chilly'
        if(tag == 'Oxfords'):
            return 'chilly'
        if(tag == 'Men\'s Sandals'):
            return 'sunny'
        if(tag == 'Umbrella'):
            return 'rain'
        if(tag == 'Loafers'):
            return 'chilly'
        if(tag == 'Boat Shoes'):
            return 'chilly'
        if(tag == 'Overalls'):
            return 'snow'
        else:
            return 'ERROR: No Such Clothing Object in database.'
    else:
        return 'Bad Flag Value'