from radar import RadarClient

# initialize client with your project's secret key and publishable key
SECRET_KEY = "<YOUR SECRET KEY>"
PUB_KEY = "<YOUR PUB KEY>"
radar = RadarClient(secret_key=SECRET_KEY, pub_key=PUB_KEY)

# Get context for a location without sending device or user identifiers to the server.
coordinates = (40.702640, -73.990810)
context = radar.context.get(coordinates=coordinates)
if "place" in dir(context):
    print(f"Location is at place: {context.place.name}")

print(context)
"""
{
  "live": false,
  "geofences": [],
  "place": {
    "_id": "5dc9ada22004860034be2f80",
    "categories": [
      "food-beverage",
      "cafe",
      "coffee-shop"
    ],
    "chain": {
      "domain": "starbucks.com",
      "name": "Starbucks",
      "slug": "starbucks"
    },
    "location": {
      "coordinates": [
        -73.990924,
        40.702719
      ],
      "type": "Point"
    },
    "name": "Starbucks"
  },
  "country": {
    "_id": "5cf694f66da6a800683f4d71",
    "code": "US",
    "name": "United States",
    "type": "country"
  },
  "state": {
    "_id": "5cf695096da6a800683f4e7f",
    "code": "NY",
    "name": "New York",
    "type": "state"
  }
  "dma": {
    "_id": "5cf695016da6a800683f4e06",
    "code": "501",
    "name": "New York",
    "type": "dma"
  },
  "postalCode": {
    "_id": "5cf695286da6a800683f5911",
    "code": "11201",
    "name": "11201",
    "type": "postalCode"
  },
}
"""
