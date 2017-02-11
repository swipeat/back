#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

import requests
import random
from datetime import datetime

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
    def __init__(self, constraints):

        super(Food2forkDish, self).__init__(constraints)

        self.url = BASE_URL + '/search'
        self.dishquery = {}

        self.original_dishes_list = []
        self.total_number_dishes = 0
        # initialize dishes and count how many we have
        self.initial_query(pages=2)

        self.current_processed_json = {}
        self.ingredients_list = {}

        # set initial seed of random generator
        random.seed(datetime.now())

    def get_dishes(self, number_of_dishes=5):
        """
        Query DB API and return list of dishes
        :param number_of_dishes: how many dishes to return
        :return: JSON of dishes with their Ids, titles, and image_urls
        """
        if not self.constraints:
            return None

        # check if we already queried API or not
        if not self.original_dishes_list:
            self.initial_query()

        # return smallest feasible number of dishes
        dishes_limit = min(self.total_number_dishes, int(number_of_dishes))
        # print("self.total_number_dishes", self.total_number_dishes)
        # print (dishes_limit)
        self.randomize_dishes_list()
        processed_json = []
        i = 0
        for dish in self.original_dishes_list:
            if i >= dishes_limit:
                break
            # keep only dish ID, title, and image url
            processed_json += [{'recipe_id' : dish[u'recipe_id'], 'title': dish[u'title'], 'image_url': dish[u'image_url']}]
            i += 1

        self.current_processed_json = processed_json
        return self.current_processed_json

    def initial_query(self, pages=1):
        sets_dishes = {}
        for constraint in self.constraints:
            for page in range(1, pages + 1):
                self.dishquery = {
                    "key": API_KEY,
                    "q": "{}".format(constraint),
                    "page": str(page)
                }
                sets_dishes[constraint] = self.query_api(self.url, self.dishquery, HEADER)
                self.total_number_dishes += int(sets_dishes[constraint][u'count'])
                self.original_dishes_list.extend(sets_dishes[constraint][u'recipes'])

    def randomize_dishes_list(self):
        # indices = numpy.array(range(self.total_number_dishes))
        # numpy.random.shuffle(indices)
        random.shuffle(self.original_dishes_list)

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
        # print ("self.dish_ids", self.dish_ids)
        for dish_id in self.dish_ids:
            dish = self.query_api(self.url, {"key": API_KEY, "rId": "{}".format(dish_id)}, HEADER)
            # print (dish)
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
        # print (url, queryrequest)
        r = requests.get(url, params=queryrequest, headers=headers)
        return r.json()
