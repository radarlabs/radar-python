from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "<YOUR SECRET KEY>"
radar = RadarClient(SECRET_KEY)

# Geocodes an address, converting address to coordinates.

address = radar.geocode.forward(query="20 jay st brooklyn")[0]
print(address)
print(f"{address.latitude}, {address.longitude}")
"""
>>> print(address)
{
  "borough": "Brooklyn",
  "city": "New York",
  "confidence": "exact",
  "country": "United States",
  "countryCode": "US",
  "countryFlag": "\ud83c\uddfa\ud83c\uddf8",
  "formattedAddress": "20 Jay Street, Brooklyn, New York, NY 11201 USA",
  "geometry": {
    "coordinates": [
      -73.986675,
      40.704262
    ],
    "type": "Point"
  },
  "latitude": 40.704262,
  "longitude": -73.986675,
  "name": "20 Jay Street",
  "neighborhood": "DUMBO",
  "number": "20",
  "postalCode": "11201",
  "state": "New York",
  "stateCode": "NY",
  "street": "Jay Street"
}
>>> print(f"{address.latitude}, {address.longitude}")
40.704262, -73.986675
"""

# Reverse geocodes a location, converting coordinates to address.

address = radar.geocode.reverse(coordinates=(40.7041895, -73.9867797))[0]
"""
>>> print(address)
{
  "borough": "Brooklyn",
  "city": "New York",
  "country": "United States",
  "countryCode": "US",
  "countryFlag": "\ud83c\uddfa\ud83c\uddf8",
  "distance": 0.015,
  "formattedAddress": "20 Jay St, Brooklyn, New York, NY USA",
  "geometry": {
    "coordinates": [
      -73.986802,
      40.704053
    ],
    "type": "Point"
  },
  "latitude": 40.704053,
  "longitude": -73.986802,
  "name": "20 Jay St",
  "neighborhood": "DUMBO",
  "number": "20",
  "state": "New York",
  "stateCode": "NY",
  "street": "Jay St"
}
>>> print(address.formattedAddress)
20 Jay St, Brooklyn, New York, NY USA
"""


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
