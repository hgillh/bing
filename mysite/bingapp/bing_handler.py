'''module to search results from bing
'''
import requests
from mysite.settings import BING_KEY, BING_SEARCH_ENDPOINT


class BingHelper():
    '''class bing helper
    '''

    def __init__(self):
        self._search_url = BING_SEARCH_ENDPOINT

    def bing_search(self, search_term):
        '''method to search from bing using bing api

        Args:
            search_term [string]: keyword to search from bing

        Return:
            json: json of response from bing API
        '''

        headers = {"Ocp-Apim-Subscription-Key": BING_KEY}
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(self._search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        return search_results
