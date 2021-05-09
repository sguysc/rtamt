# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.abstract_evaluator import AbstractEvaluator

NOT_IMPLEMENTED = "You should implement this."

class OfflineEvaluator(AbstractEvaluator):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: so far it does nothing. we need to think what we need to do here.

    __metaclass__ = ABCMeta

    def __init__(self):
        super(AbstractEvaluator, self).__init__()

    @abstractmethod
    def evaluate(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)