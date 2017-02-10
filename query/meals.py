#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

from query.mealsearcher import MealSearcher
from .singleton import *


@Singleton
class Meals(object):
    """
    General class to mealquery meals from either recipes databases, APIs, or cached recipes.
    """
    def __init__(self,
                 query_object
                 ):
        self.query_object = None
        if query_object is not None:
            self.set_query_object(query_object)

    def set_query_object(self, query_object):
        """
        :param query_object: set the current MealSearcher that searchers for meals
        """
        assert (query_object is None)
        assert isinstance(self.query_object, MealSearcher)
        self.query_object = query_object

    def get_query_object(self):
        """
        :return: current MealSearcher used for searching meals
        """
        return self.query_object

    def get_meals(self, number_of_meals=5):
        return self.query_object.get_meals(number_of_meals)