from geopy.geocoders import Nominatim
from .utils import get_geo, get_center_coordinates, get_ip_address
geolocator = Nominatim(user_agent ="")

def index(request):
    urls = "http://api.eia.gov/series/?api_key=635b484a4b605642bbbf459439cc943f&series_id="

  # getting latitude and longitude

    if request.method == 'POST':
        latitude = request.POST['lat']
        print (latitude)
        longitude = request.POST['long']
        print (longitude)

   # reverse geolocation to find the address

    location = geolocator.reverse((latitude, longitude))
    location = str(location)
    print(location)
    a = location.split(",")
    length = len(a)
    
    # find the name of the place. 

    for i in range(length):
        doc = (a[i].strip())
        if (show.filter(city_state__icontains= doc)):
            print("found")
            print(doc)
            place = doc
            
    
