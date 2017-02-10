#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

import abc
import six


class MealSearcher(six.with_metaclass(abc.ABCMeta, object)):
    """
    General class that provides API for querying recipes databases, APIs, or cached recipes.
    """
    def __init__(self, queryrequest):
        self.queryrequest = str(queryrequest)

    @abc.abstractmethod
    def get_meals(self, number_of_meals=5):
        """
        :param number_of_meals: how many meals from the underlying API to return
        :return: Returns JSON description of meals
        """
        raise NotImplementedError("Please implement this function in derived classes")