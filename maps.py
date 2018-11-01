import googlemaps
from gmplot import gmplot
from datetime import datetime

api_key='AIzaSyDDNYRDYmhnIuu4UGowg0ozgOkYkT_uImo'
# gmaps = googlemaps.Client(key=api_key)
# # Geocoding an address
# geocode_result = gmaps.geocode('Hyderabad')[0]
# lat = geocode_result['geometry']['location']['lat']
# lng = geocode_result['geometry']['location']['lng']
# print(lng)
#
# from gmplot import gmplot
# #Place map
# gmap = gmplot.GoogleMapPlotter(lat, lng, 5)
# gmap.draw('index.html')
# import googlemaps
# from datetime import datetime

gmaps = googlemaps.Client(key=api_key)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)