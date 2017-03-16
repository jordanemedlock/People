from location import Location
from temboo.Library.Labs import GetWeather
from temboo.core.session import TembooSession
import json
from capability import Capability
from powertypes import PowerDict


class Weather(PowerDict, Capability):
    def __init__(self, info={}, session=None, person=None):
        self.session = session or TembooSession("jordanemedlock", "jordanemedlockcom", "aB8hQizrTLhyOUitwNdnxvddWa3Fw6ZG")
        self.weather = None
        PowerDict.__init__(self, info)
        Capability.__init__(self, person)

    def __json__(self):
        return self

    @classmethod
    def from_json(cls, info):
        return cls(info=info)

    def intent_response(self, intent):
        return "" # TODO: Alex

    def get_weather(self, loc):
        choreo = GetWeather.ByCoordinates(self.session)
        inputs = choreo.new_input_set()
        inputs.set_Latitude(str(loc.lat()))
        inputs.set_Longitude(str(loc.lon()))
        self.weather = json.loads(choreo.execute_with_results(inputs).get_Response())
        return self.weather


if __name__ == "__main__":
    weather = Weather()
    loc = Location(address="520 14th st 87102")
    weather_data = weather.get_weather(loc)
    print(weather_data['high'])
    print(weather_data['low'])
    print(weather_data['temperature'])
    print(weather_data['forecast'])