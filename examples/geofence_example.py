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

# get a geofence by tag and externalId
geofence = radar.geofences.get(tag="store", externalId="123")
print(geofence)

# list geofences
for geofence in radar.geofences.list():
    print(f"Geofence: {geofence._id} - {geofence.description}")

# list users in a geofence
users_in_geofence = radar.geofences.list_users(tag="store", externalId="123")

# delete a geofence, can call geofence.delete() if it's already been fetched
radar.geofences.delete(tag="store", externalId="123")
