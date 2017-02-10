#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

import json
import requests
from query.mealsearcher import MealSearcher
from query.ingredientsearcher import IngredientSearcher

BASE_URL = 'https://community-food2fork.p.mashape.com'
# API KEY can be obtained by registering at food2fork.com
API_KEY = 'b8b3e86ad3ee196ec2aff15d6a05579f'

HEADER = {
    "X-Mashape-Key": "0hDYGmL5grmsh197WzPKPsg9ozTDp11YISzjsnDDV8aUUN0P81",
    "Accept": "application/json"
}


class Food2forkMeal(MealSearcher):
    """
    Implementation of MealSearcher interface for food2fork.com recipe API
    """
    def __init__(self, queryrequest):

        super(Food2forkMeal, self).__init__(queryrequest)

        self.url = BASE_URL + '/search'

        self.mealquery = {
            "key": API_KEY,
            "q": "{}".format(queryrequest)
        }

        self.original_meals_json = self.query_api(self.url, self.mealquery, HEADER)
        self.current_processed_json = {}

        self.ingredients_list = {}

    def get_meals(self, number_of_meals=5):
        """
        Query DB API and return list of meals
        :param number_of_meals: how many meals to return
        :return: JSON of meals with their Ids, titles, and image_urls
        """
        # check if we already queried API or not
        if not self.original_meals_json:
            self.original_meals_json = self.query_api(self.url, self.mealquery, HEADER)
        # return smallest feasible number of meals
        meals_limit = min(int(self.original_meals_json[u'count']), int(number_of_meals))
        processed_json = {}
        i = 0
        for meal in self.original_meals_json[u'recipes']:
            if i >= meals_limit:
                break
            # keep only meal ID, title, and image url
            processed_json[meal[u'recipe_id']] = {'title': meal[u'title'], 'image_url': meal[u'image_url']}
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

    # def current_meals_ingredients(self):
    #     ingredients_list = {}
    #     for meal_id, meal in self.current_processed_json.iteritems():
    #         ingredients_list[meal_id] = Food2forkIngredients(meal_id)
    #     self.ingredients_list = ingredients_list
    #     return self.ingredients_list
    #
    # def current_ingredients_json(self):
    #     if not self.ingredients_list:
    #         self.ingredients_list = self.current_meals_ingredients()
    #     json_list = []
    #     for meal_id, ingred_obj in self.ingredients_list.iteritems():
    #         assert isinstance(ingred_obj, IngredientSearcher)
    #         json_list.extend(ingred_obj.get_ingredients())
    #     return json.dumps({"ingredients": json_list})


class Food2forkIngredients(IngredientSearcher):
    """
    Implementation of IngredientSearcher interface for food2fork.com recipe API
    """
    def __init__(self, meal_ids):

        super(Food2forkIngredients, self).__init__(meal_ids)

        self.url = BASE_URL + '/get'
        self.headers = {
            "X-Mashape-Key": "0hDYGmL5grmsh197WzPKPsg9ozTDp11YISzjsnDDV8aUUN0P81",
            "Accept": "application/json"
        }
        self.ingredients_list = None

    def get_ingredients(self):
        # if we did not initialized meal_ids, error out
        if not self.meal_ids:
            return None
        assert isinstance(self.meal_ids, list)
        # do not query if the list already exists
        if self.ingredients_list:
            return self.ingredients_list

        self.ingredients_list = []
        print ("self.meal_ids", self.meal_ids)
        for meal_id in self.meal_ids:
            meal = self.query_api(self.url, {"key": API_KEY, "rId": "{}".format(meal_id)}, HEADER)
            print (meal)
            self.ingredients_list.extend(meal[u'recipe'][u'ingredients'])

        return json.dumps({"ingredients": self.ingredients_list})

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
