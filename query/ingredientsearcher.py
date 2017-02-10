#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

import abc
import six


class IngredientSearcher(six.with_metaclass(abc.ABCMeta, object)):
    """
    General class that provides API for querying ingredients databases, APIs, or cached ingredients.
    """
    def __init__(self, meal_ids):
        self.meal_ids = str(meal_ids)

    @abc.abstractmethod
    def get_ingredients(self):
        """
        :return: Returns JSON description of ingredients
        """
        raise NotImplementedError("Please implement this function in derived classes")