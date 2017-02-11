#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

from query.dishsearcher import searcher import DishSearcher
from .singleton import *


@Singleton
class Dishes(object):
    """
    General class to dishquery dishes from either recipes databases, APIs, or cached recipes.
    """
    def __init__(self):
        self.query_object = None

    def set_query_object(self, query_object):
        """
        :param query_object: set the current DishSearcher that searchers for dishes
        """
        assert (query_object is not None)
        assert isinstance(query_object, DishSearcher)
        self.query_object = query_object

    def get_query_object(self):
        """
        :return: current DishSearcher used for searching dishes
        """
        return self.query_object

    def get_dishes(self, number_of_dishes=5):
        return self.query_object.get_dishes(number_of_dishes)