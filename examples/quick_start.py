from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "<YOUR SECRET KEY>"
radar = RadarClient(SECRET_KEY)

# create a geofence
data = {
    "description": "Example Store",
    "type": "circle",
    "coordinates": [-73.98706, 40.7041029],
    "radius": 100,
    "tag": "store",
    "externalId": "123",
}
new_geofence = radar.geofences.create(data=data)

# Geocode an IP address, converting IP address to country, state if available

ip_location = radar.geocode.ip(ip="107.77.199.117")
"""
>>> print(ip_location)
{
  "city": "Atoka",
  "country": "United States",
  "countryCode": "US",
  "countryFlag": "\ud83c\uddfa\ud83c\uddf8",
  "latitude": 34.385929107666016,
  "longitude": -96.12832641601562,
  "meta": {
    "code": 200
  },
  "postalCode": "74525",
  "state": "Oklahoma",
  "stateCode": "OK"
}
"""

# Compare a route by bike vs foot

origin = (40.7041029, -73.98706)
destination = (40.7141029, -73.99706)
routes = radar.route.distance(origin, destination, modes="bike,foot")
"""
>>> print(f"by foot: {routes.foot}\nby bike: {routes.bike}")
by foot: <distance=2.8 km duration=34 mins>
by bike: <distance=3.2 km duration=12 mins>
"""

# Let a user know what hotels are nearby using place search
user_location = (40.7043, -73.9867)
radar.search.places(near=user_location, categories="hotel-lodging")
"""
[
    <Radar Place: _id='5ded545230409c49f439d943' name='1 Hotel Brooklyn Bridge' categories=['hotel-lodging', 'hotel']>,
    <Radar Place: _id='59c1f5898be4c5ce940b559f' name='Dazzler Hotels' categories=['hotel-lodging', 'inn', 'hotel', 'resort']>,
    <Radar Place: _id='59bf2f8d8be4c5ce9409d9f9' name='Hotel St. George' categories=['hotel-lodging', 'hotel']>,
    <Radar Place: _id='5ded528630409c49f41b36a1' name='Hampton Inn' categories=['hotel-lodging', 'hotel']>,
    <Radar Place: _id='59c1f5898be4c5ce940b559c' name='Hampton Inn Brooklyn Downtown' categories=['hotel-lodging', 'hotel', 'inn']>
]
"""
