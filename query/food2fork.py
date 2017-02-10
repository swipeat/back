#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017


import requests
from .mealsearcher import MealSearcher

BASE_URL = 'https://community-food2fork.p.mashape.com'
# API KEY can be obtained by registering at food2fork.com
API_KEY = 'b8b3e86ad3ee196ec2aff15d6a05579f'


class OpenFood(MealSearcher):
    """
    Implementation of MealSearcher interface for food2fork.com recipe API
    """
    def __init__(self, queryrequest):

        super(OpenFood, self).__init__(queryrequest)

        self.url = BASE_URL + '/search'

        self.query = {
            "key": API_KEY,
            "q": "{}".format(queryrequest)
        }

        self.headers = {
            "X-Mashape-Key": "0hDYGmL5grmsh197WzPKPsg9ozTDp11YISzjsnDDV8aUUN0P81",
            "Accept": "application/json"
        }
        self.results_json = self.query_api(self.url, self.query, self.headers)

    def get_meals(self, number_of_meals=5):
        return self.results_json

    def query_api(self, url, queryrequest, headers):
        return requests.get(url, params=queryrequest, headers=headers)
