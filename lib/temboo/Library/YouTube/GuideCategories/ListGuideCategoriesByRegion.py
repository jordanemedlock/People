# -*- coding: utf-8 -*-

###############################################################################
#
# ListGuideCategoriesByRegion
# Returns a list of guide categories available in the specified country.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListGuideCategoriesByRegion(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListGuideCategoriesByRegion Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListGuideCategoriesByRegion, self).__init__(temboo_session, '/Library/YouTube/GuideCategories/ListGuideCategoriesByRegion')


    def new_input_set(self):
        return ListGuideCategoriesByRegionInputSet()

    def _make_result_set(self, result, path):
        return ListGuideCategoriesByRegionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListGuideCategoriesByRegionChoreographyExecution(session, exec_id, path)

class ListGuideCategoriesByRegionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListGuideCategoriesByRegion
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('Fields', value)
    def set_H1(self, value):
        """
        Set the value of the H1 input for this Choreo. ((optional, string) The hl parameter specifies the language that should be used for text values in the API response. The default value is en_US.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('H1', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of one or more guideCategory resource properties that the API response will include. Valid values are: id and snippet.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('RefreshToken', value)
    def set_RegionCode(self, value):
        """
        Set the value of the RegionCode input for this Choreo. ((optional, string) Indicates to return the list of guide categories available in the specified country. The parameter value is an ISO 3166-1 alpha-2 country code. Defaults to US.)
        """
        super(ListGuideCategoriesByRegionInputSet, self)._set_input('RegionCode', value)

class ListGuideCategoriesByRegionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListGuideCategoriesByRegion Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)

class ListGuideCategoriesByRegionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListGuideCategoriesByRegionResultSet(response, path)
