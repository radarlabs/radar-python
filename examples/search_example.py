from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "<YOUR SECRET KEY>"
radar = RadarClient(SECRET_KEY)

# Search for users near a store to send a promotional offer
store_location = (40.7043, -73.9867)
users = radar.search.users(near=store_location)
for user in users:
    # send a push notification
    pass

# Power a store locator using geofence search
user_location = (40.7043, -73.9867)
nearby_stores = radar.search.geofences(near=user_location, tags="store", limit=10)

# Let a user know what hotels are nearby using place search
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

# Power a destination selector using address autocomplete
radar.search.autocomplete(query="20 jay st", near=user_location)
"""
[
    <Radar Address: latitude=40.703945 longitude=-73.98671 formattedAddress='20 Jay Street, Brooklyn, New York, NY 11201 USA'>,
    <Radar Address: latitude=40.717976 longitude=-74.010188 formattedAddress='20 Jay St, Manhattan, New York, NY 10013 USA'>,
    <Radar Address: latitude=40.74862 longitude=-74.181978 formattedAddress='20 Jay St, Newark, NJ USA'>,
    <Radar Address: latitude=40.923457 longitude=-74.170418 formattedAddress='20 Jay Street, Paterson, NJ USA'>,
    <Radar Address: latitude=40.908339 longitude=-74.510157 formattedAddress='20 Jay St, Rockaway, NJ USA'>
]
"""
