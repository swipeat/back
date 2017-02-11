#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Pavel Korshunov <pavelkor@gmail.com>
# @date: Fri 10 Feb 18:43:22 2017

import abc
import six


class DishSearcher(six.with_metaclass(abc.ABCMeta, object)):
    """
    General class that provides API for querying recipes databases, APIs, or cached recipes.
    """
    def __init__(self, queryrequest):
        self.queryrequest = str(queryrequest)
        self.title = None
        self.image_url = None

    @abc.abstractmethod
    def get_dishes(self, number_of_dishes=5):
        """
        :param number_of_dishes: how many dishes from the underlying API to return
        :return: Returns JSON description of dishes
        """
        raise NotImplementedError("Please implement this function in derived classes")