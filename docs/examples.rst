Examples
********

.. contents:: Contents
   :local:

Quick Start
---------

Want to jump right in? Below is a quick overview of how to get started using the radar-python library to power location based applications.  Signup for your free account here https://radar.io/signup and grab your API keys to get started.

.. literalinclude:: ../examples/quick_start.py

Initialization
--------------

Everything goes through the radar client, so start by initializing RadarClient with your API keys::

    >>> from radar import RadarClient
    >>> radar = RadarClient('secret')

The radar client provides access to all the radar API's such as geofences, places, geocoding, search. Examples for each endpoint are included below.

Geofences
---------

Geofences represent custom regions or places monitored in your project. Depending on your use case, a geofence might represent a retail store, a neighborhood, and so on.

Radar geofencing is more powerful than native iOS or Android geofencing, with cross-platform support for unlimited geofences, polygon geofences, and stop detection.

https://radar.io/documentation/geofences

.. literalinclude:: ../examples/geofence_example.py

Events
------

An event represents a change in user state. Events can be uniquely referenced by Radar ``_id``.

https://radar.io/documentation/api#events

.. literalinclude:: ../examples/event_example.py

Using this method, authentication happens during then initialization of the object. If the authentication is successful,
the retrieved session cookie will be used in future requests. Upon cookie expiration, authentication will happen again transparently. 

Users
-----

A user represents a user tracked in your project. Users can be referenced by Radar ``_id``, ``userId``, or ``deviceId``

https://radar.io/documentation/api#users

.. literalinclude:: ../examples/user_example.py


Context
-------

Gets context for a location without sending device or user identifiers to the server.

https://radar.io/documentation/api#context

.. literalinclude:: ../examples/context_example.py


Search
------

https://radar.io/documentation/api#search

.. literalinclude:: ../examples/search_example.py

Geocode
-------

https://radar.io/documentation/api#geocode

.. literalinclude:: ../examples/geocode_example.py

Route
-------

https://radar.io/documentation/api#route

.. literalinclude:: ../examples/route_example.py
