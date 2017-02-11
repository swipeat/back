#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

import json
import requests
from query.dishsearcher import DishSearcher
from query.ingredientsearcher import IngredientSearcher

BASE_URL = 'https://community-food2fork.p.mashape.com'
# API KEY can be obtained by registering at food2fork.com
API_KEY = 'b8b3e86ad3ee196ec2aff15d6a05579f'

HEADER = {
    "X-Mashape-Key": "0hDYGmL5grmsh197WzPKPsg9ozTDp11YISzjsnDDV8aUUN0P81",
    "Accept": "application/json"
}


class Food2forkDish(DishSearcher):
    """
    Implementation of DishSearcher interface for food2fork.com recipe API
    """
    def __init__(self, queryrequest):

        super(Food2forkDish, self).__init__(queryrequest)

        self.url = BASE_URL + '/search'

        self.dishquery = {
            "key": API_KEY,
            "q": "{}".format(queryrequest)
        }

        self.original_dishes_json = self.query_api(self.url, self.dishquery, HEADER)
        self.current_processed_json = {}

        self.ingredients_list = {}

    def get_dishes(self, number_of_dishes=5):
        """
        Query DB API and return list of dishes
        :param number_of_dishes: how many dishes to return
        :return: JSON of dishes with their Ids, titles, and image_urls
        """
        # check if we already queried API or not
        if not self.original_dishes_json:
            self.original_dishes_json = self.query_api(self.url, self.dishquery, HEADER)
        # return smallest feasible number of dishes
        dishes_limit = min(int(self.original_dishes_json[u'count']), int(number_of_dishes))
        processed_json = {}
        i = 0
        for dish in self.original_dishes_json[u'recipes']:
            if i >= dishes_limit:
                break
            # keep only dish ID, title, and image url
            processed_json[dish[u'recipe_id']] = {'title': dish[u'title'], 'image_url': dish[u'image_url']}
            i += 1

        self.current_processed_json = json.dumps(processed_json)
        return self.current_processed_json

    def query_api(self, url, queryrequest, headers):
        """
        Query the food2fork DB API
        :param url:
        :param queryrequest:
        :param headers:
        :return:
        """
        r = requests.get(url, params=queryrequest, headers=headers)
        return r.json()

    # def current_dishes_ingredients(self):
    #     ingredients_list = {}
    #     for dish_id, dish in self.current_processed_json.iteritems():
    #         ingredients_list[dish_id] = Food2forkIngredients(dish_id)
    #     self.ingredients_list = ingredients_list
    #     return self.ingredients_list
    #
    # def current_ingredients_json(self):
    #     if not self.ingredients_list:
    #         self.ingredients_list = self.current_dishes_ingredients()
    #     json_list = []
    #     for dish_id, ingred_obj in self.ingredients_list.iteritems():
    #         assert isinstance(ingred_obj, IngredientSearcher)
    #         json_list.extend(ingred_obj.get_ingredients())
    #     return json.dumps({"ingredients": json_list})


class Food2forkIngredients(IngredientSearcher):
    """
    Implementation of IngredientSearcher interface for food2fork.com recipe API
    """
    def __init__(self, dish_ids):

        super(Food2forkIngredients, self).__init__(dish_ids)

        self.url = BASE_URL + '/get'
        self.headers = {
            "X-Mashape-Key": "0hDYGmL5grmsh197WzPKPsg9ozTDp11YISzjsnDDV8aUUN0P81",
            "Accept": "application/json"
        }
        self.ingredients_list = None

    def get_ingredients(self):
        # if we did not initialized dish_ids, error out
        if not self.dish_ids:
            return None
        assert isinstance(self.dish_ids, list)
        # do not query if the list already exists
        if self.ingredients_list:
            return self.ingredients_list

        self.ingredients_list = []
        print ("self.dish_ids", self.dish_ids)
        for dish_id in self.dish_ids:
            dish = self.query_api(self.url, {"key": API_KEY, "rId": "{}".format(dish_id)}, HEADER)
            print (dish)
            self.ingredients_list.extend(dish[u'recipe'][u'ingredients'])

        return {"ingredients": self.ingredients_list}
        #return json.dumps({"ingredients": self.ingredients_list})

    def query_api(self, url, queryrequest, headers):
        """
        Query food2fork DB API for ingredients
        :param url:
        :param queryrequest:
        :param headers:
        :return:
        """
        print (url, queryrequest)
        r = requests.get(url, params=queryrequest, headers=headers)
        return r.json()
