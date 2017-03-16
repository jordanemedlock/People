from temboo.Library.Labs import GetWeather, GetPlaces
from temboo.Library.Google import Geocoding
from temboo.core.session import TembooSession
import json

class Location(object):
    def __init__(self, lat=None, lon=None, address=None):
        self.session = TembooSession("jordanemedlock", "jordanemedlockcom", "aB8hQizrTLhyOUitwNdnxvddWa3Fw6ZG")
        self._address = address
        self._lat = lat
        self._lon = lon

    def lat_lon(self):
        if self._lat is None:
            choreo = Geocoding.GeocodeByAddress(self.session)
            inputs = choreo.new_input_set()
            inputs.set_Address(self.address())
            results = choreo.execute_with_results(inputs)
            lat, lon = results.get_Latitude(), results.get_Longitude()
            self._lat = lat
            self._lon = lon
        return (float(self._lat), float(self._lon))

    def address(self):
        if self._address is None:
            choreo = Geocoding.GeocodeByCoordinates(self.session)
            inputs = choreo.new_input_set()
            inputs.set_Latitude(str(self.lat()))
            inputs.set_Longitude(str(self.lon()))
            results = choreo.execute_with_results(inputs)
            self._address = results.get_FormattedAddress()
        return self._address

    def lat(self):
        if self._lon is None:
            self._lat, self._lon = self.lat_lon()
        return self._lat

    def lon(self):
        if self._lon is None:
            self._lat, self._lon = self.lat_lon()
        return self._lon

    def places(self, creds):
        choreo = GetPlaces.ByCoordinates(self.session)
        inputs = choreo.new_input_set()
        inputs.set_APICredentials(creds)
        inputs.set_Latitude(str(self.lat()))
        inputs.set_Longitude(str(self.lon()))
        results = choreo.execute_with_results(inputs)
        return results.get_Response()


if __name__ == "__main__":
    loc = Location(address="2100 Airpark rd 87106")
    print(loc.lat())
    print(loc.lon())
    print(loc.weather())



