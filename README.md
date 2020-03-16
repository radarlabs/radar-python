# radar-python
Python library for the [Radar API](https://radar.io/documentation/api)

* **[Docs](https://radar-python.readthedocs.io/en/latest/)** 
* **[PyPi](https://pypi.org/project/radar-python/)**

The Radar Python library provides convenient access to Radar's APIs from
your python applications or command line.

[![CircleCI](https://circleci.com/gh/radarlabs/radar-python/tree/master.svg?style=svg)](https://circleci.com/gh/radarlabs/radar-python/tree/master)

# Installation

You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

```sh
pip install radar-python
```

## Requirements
Python 3.4+

# Usage

The radar client needs to be initialized with your project’s secret key which is available in your [Radar Dashboard](https://radar.io/dashboard/settings). 

```python
import os
from radar import RadarClient
 
# initialize client
radar = RadarClient(os.environ["RADAR_SECRET_KEY"])
 
# get a geofence by id
geofence = radar.geofences.get(id='123')
 
# list geofences
radar.geofences.list()
```


# Full Endpoint List:
### Users:
```
radar.users.list
radar.users.get(id='1')
radar.users.delete(id='1')
```

### Geofences
```
radar.geofences.list()
radar.geofences.get(id=’123’)
radar.geofences.get(tag=’store’, externalId=’123’)
radar.geofences.list_users(id='123')
radar.geofences.create({ 'type': 'circle', ... })
radar.geofences.delete(id='123')
radar.geofences.delete(tag=’store’, externalId=’123’)
```

### Events
```
radar.events.list()
radar.events.get(id='123')
radar.events.delete(id='123')
radar.events.verify(id='123', 'accept')
```

### Context
```
radar.context.get(coordinates=(40.7041895, -73.9867797))
```

### Geocoding
```
radar.geocode.forward(query=’20 jay st brooklyn’)
radar.geocode.reverse(coordinates=(40.7041895, -73.9867797))
radar.geocode.ip(ip=’107.77.199.117’)
```

### Search
```
radar.search.users(near=[lat,long])
radar.search.geofences(near=[lat,long])
radar.search.places(near=[lat,long])
radar.search.autocomplete(query=’20 jay st’, near=[lat, long])
```

### Routing
```
radar.route.distance(origin=[lat,lng], destination=[lat,lng], modes=’car’, units=’metric’)
```
