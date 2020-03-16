from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "<YOUR SECRET KEY>"
radar = RadarClient(SECRET_KEY)

# Compare a route by bike vs foot

origin = (40.7041029, -73.98706)
destination = (40.7141029, -73.99706)
routes = radar.route.distance(origin, destination, modes="bike,foot")
"""
>>> print(f"by foot: {routes.foot}\nby bike: {routes.bike}")
by foot: <distance=2.8 km duration=34 mins>
by bike: <distance=3.2 km duration=12 mins>
"""

# Whats the quickest way to get from a user's origin to destination?

origin = (40.7041029, -73.98706)
destination = (40.7141029, -73.99706)
routes = radar.route.distance(origin, destination, modes="transit,car,bike,foot")

(quickest_mode, quickest_route) = min(
    [("car", routes.car), ("transit", routes.transit), ("bike", routes.bike)],
    key=lambda route: route[1].duration.value,
)
"""
>>> print(f"quickest route is by {quickest_mode}, which will take {quickest_route.duration.value:.2f} min")
quickest route is by car, which will take 9.57 min
"""
