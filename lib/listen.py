
from capability import Capability
from powertypes import PowerDict
from location import Location

class Listen(PowerDict, Capability):
    def __init__(self, parent=None, info={}):
        Capability.__init__(self, parent)
        PowerDict.__init__(self, info)

    def __call__(self, msg):
        text = msg["text"]
        if 'weather' in text.lower():
            weather = self.parent['weather'].get_weather(Location(address='87112'))
            return 'The weather for today will be ' + weather['text'] + ' with a high of ' + weather['high']
        return text

    def __json__(self):
        return self

    @staticmethod
    def from_json(obj):
        return Listen(info=obj)
