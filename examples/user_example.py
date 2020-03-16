from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "<YOUR SECRET KEY>"
radar = RadarClient(SECRET_KEY)

# get a user by _id, externalId, or deviceId
user = radar.user.get("123")
print(user)

# list the 50 most recently updated users, and any geofences they're in
for user in radar.users.list(limit=50):
    print(f"User: {user._id}, last updated at {user.updatedAt}")
    for geofence in user.geofences:
        print(f"...in geofence {geofence.description}")

# delete a user, can call user.delete() if it's already been fetched
radar.users.delete("123")
