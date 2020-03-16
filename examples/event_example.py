from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "<YOUR SECRET KEY>"
radar = RadarClient(SECRET_KEY)

# get an event by id
event = radar.events.get(id="123")
print(event)

# list events
for event in radar.events.list():
    print(f"Event: {event.type} at {event.createdAt}")

# list events from a certain time window
from datetime import datetime, timedelta, time

yesterday = datetime.now() - timedelta(days=1)
yesterday_9am = datetime.combine(yesterday, time(9))
yesterday_11am = datetime.combine(yesterday, time(11))
radar.events.list(createdAfter=yesterday_9am, createdBefore=yesterday_11am)

# verify an event
radar.events.verify(id="123", "accept")
radar.events.verify(id="123", value=1)

# delete an event, can call event.delete() if it's already been fetched
radar.events.delete(id="123")
