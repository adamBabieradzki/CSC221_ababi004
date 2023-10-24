def location(city,country,population=None):
    if population != None: 
        return f'{city}, {country} population - {population}'
    else: return f'{city}, {country}'