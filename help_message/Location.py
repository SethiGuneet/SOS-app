import geocoder
g = geocoder.ip('me')
print(g.lat)
print(g.lng)
print(g.latlng)

# BASICALLY FOR TESTING A LOCATION FINDER
