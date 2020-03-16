import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCzHi5h2Gf5OoPRV_kkZxJimuU8p1RQGyw')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result)
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
