
def city_country(_city, _country):
    location = {
        'city' : _city,
        'country' : _country
    }

    #return location
    return location



while True:
    
    city = str(input("press q and hit enter to quit anytime... \nYou're city: ")).lower()
    country = str(input("You're country: ")).lower()

    #passing the argument to funtion
    if city == 'q' or country == 'q':
        break

    display_info = city_country(city, country)
    print(f"{display_info['city']}, {display_info['country']}")
    