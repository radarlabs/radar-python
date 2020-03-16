import json
from radar.utils import obj_to_dict


class Model:
    OBJECT_NAME = "Model"

    def __init__(self, radar, data={}):
        """Initialize a Radar Model instance

        Args:
            radar (RadarClient): RadarClient for instance CRUD actions
            raw_json (dict): raw data to initialize the model with
        """
        self._radar = radar
        self.raw_json = data
        for attribute, value in data.items():
            setattr(self, attribute, value)

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

    def __repr__(self):
        """Identify the class and include relevant values."""
        names = []
        if self.raw_json:
            for name in self._DISPLAY_ATTRIBUTES:
                if name in self.raw_json:
                    names.append(name + "=" + repr(getattr(self, name)))
        formatted_names = " ".join(names)
        return f"<Radar {self.OBJECT_NAME}: {formatted_names}>"

    def to_dict(self):
        return obj_to_dict(self)
