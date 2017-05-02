def tagsToTags(tag,flag):
    if(flag == 0):
    #body location functional tags
        if(tag == 'Gloves'):
            return 'hands'
        if(tag == 'Women\'s Boots'):
            return 'feet'
        if(tag == 'Blazer'):
            return 'torso'
        if(tag == 'Capris'):
            return 'pants'
        if(tag == 'Leather Jacket'):
            return 'torso'
        if(tag == 'Peacoat'):
            return 'torso'
        if(tag == 'Sneakers'):
            return 'feet'
        if(tag == 'Puffy Coat'):
            return 'torso'
        if(tag == 'Men\'s Hat'):
            return 'head'
        if(tag == 'Bomber Jacket'):
            return 'torso'
        if(tag == 'Cocktail Dress'):
            return 'torso'
        if(tag == 'T-Shirt'):
            return 'torso'
        if(tag == 'Fleece Jacket'):
            return 'torso'
        if(tag == 'Kimonos'):
            return 'torso'
        if(tag == 'Pumps'):
            return 'feet'
        if(tag == 'Cardigan'):
            return 'torso'
        if(tag == 'Men\'s Dress Shoes'):
            return 'feet'
        if(tag == 'Men\'s Boots'):
            return 'feet'
        if(tag == 'Button-Down'):
            return 'torso'
        if(tag == 'Robe'):
            return 'torso'
        if(tag == 'Skinny Pants'):
            return 'legs'
        if(tag == 'Sweatshirt'):
            return 'torso'
        if(tag == 'Tights'):
            return 'legs'
        if(tag == 'Raincoats'):
            return 'torso'
        if(tag == 'Women\'s Hat'):
            return 'head'
        if(tag == 'Wide Leg Pants'):
            return 'legs'
        if(tag == 'Polos'):
            return 'torso'
        if(tag == 'Relaxed Pants'):
            return 'legs'
        if(tag == 'Denim Jacket'):
            return 'torso'
        if(tag == 'Socks'):
            return 'feet'
        if(tag == 'Hoodies'):
            return 'torso'
        if(tag == 'Women\'s Sandals'):
            return 'feet'
        if(tag == 'Platform Shoes'):
            return 'feet'
        if(tag == 'Vest'):
            return 'torso'
        if(tag == 'Spring Jacket'):
            return 'torso'
        if(tag == 'Wristlet & Clutch'):
            return 'torso'
        if(tag == 'Tracksuit'):
            return 'torso'
        if(tag == 'Oxfords'):
            return 'feet'
        if(tag == 'Men\'s Sandals'):
            return 'feet'
        if(tag == 'Umbrella'):
            return 'extra'
        if(tag == 'Loafers'):
            return 'feet'
        if(tag == 'Boat Shoes'):
            return 'feet'
        if(tag == 'Overalls'):
            return 'legs'
        else:
            return 'ERROR: No Such Clothing Object in database.'
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
