#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

from .ingredientsearcher import IngredientSearcher
from .singleton import *


@Singleton
class Ingredient(object):
    """
    General class to query ingredients from either ingredients databases, APIs, or cached ingredients.
    """
    def __init__(self,
                 query_object
                 ):
        self.query_object = None
        if query_object is not None:
            self.set_query_object(query_object)

    def set_query_object(self, query_object):
        """
        :param query_object: set the current IngredientSearcher that searchers for ingredients
        """
        assert (query_object is None)
        assert isinstance(self.query_object, IngredientSearcher)
        self.query_object = query_object

    def get_query_object(self):
        """
        :return: current IngredientSearcher used for searching ingredients
        """
        return self.query_object

    def get_ingredients(self):
        return self.query_object.get_ingredients()