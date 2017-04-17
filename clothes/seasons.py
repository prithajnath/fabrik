def seasons(tag):
    if(tag == ('\'Blazer'||'\'Bomber Jacket')):
        return 'fall'
    if(tag == ('\'Capris'||'\'Cocktail Dress'||'\'Robe'||'\"Women\'s Sandals'||'\"Men\'s Sandals')):
        return 'summer'
    if(tag == '\'Puffy Coat'):
        return 'winter'
    if(tag == '\'Spring Jacket'):
        return 'spring'
    if(tag == ('\'Gloves'||'\"Women\'s Boots'||'\'Peacoat'||'\'Fleece Jacket'||'\'Cardigan'||'\"Men\'s Boots'||'\'Sweatshirt')):
        return 'winter fall'
    if(tag == ('\'Pumps'||'\'Platform Shoes'||'\'Loafers'||'\'Boat Shoes')):
        return 'spring summer'
    if(tag == ('\'Denim Jacket'||'\'Hoodies'||'\'Overalls')):
        return 'spring fall'
    if(tag == ('\'Leather Jacket'||'\'Umbrella'||'\'Oxfords'||'\'T-Shirt'||'\'Kimonos'||'\"Men\'s Dress Shoes'||'\'Button-Down'||'\'Tights'||'\'Raincoats'||'\'Polos'||'\'Relaxed Pants'||'\'Vest'||'\'Tracksuit')):
        return 'spring summer fall'
    if(tag == ('\'Sneakers'||'\"Men\'s Hat'||'\'Skinny Pants'||'\"Women\'s Hat'||'\'Wide Leg Pants'||'\'Socks'||'\'Wristlet & Clutch')):
        return 'spring summer fall winter'
    else:
        return 'ERROR: No Such Clothing Object in database.'
