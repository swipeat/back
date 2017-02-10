#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017


import requests
from query.ingredientsearcher import IngredientSearcher

BASE_URL = 'https://www.openfood.ch/api/v2'
# API KEY can be obtained by registering at food2fork.com
API_KEY = '1300cae7207c777103ac9e6e30035c8e'


class OpenFood(IngredientSearcher):
    """
    Implementation of MealSearcher interface for food2fork.com recipe API
    """
    def __init__(self, model_ids):

        super(OpenFood, self).__init__(model_ids)

        self.url = BASE_URL + '/products'

        self.query = {
            "key": API_KEY,
            "q": "{}".format(model_ids)
        }

        self.headers = {
            'Authorization': "Token token={}".format(API_KEY),
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }
        self.results_json = self.query_api(self.url, self.query, self.headers)

    def get_ingredients(self):
        return self.results_json

    def query_api(self, url, queryrequest, headers):
        return requests.get(url, params=queryrequest, headers=headers)

