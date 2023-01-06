from .constants import *


class Planet:
    def __init__(self, name, r, i, traits=Trait.NONE, skips=Skip.N, legendary=False):
        self.__name = name
        self.__resources = r
        self.__influence = i
        self.__traits = traits
        self.__skips = skips
        self.__legendary = legendary

    def get_resource_and_influence(self):
        return self.__resources, self.__influence
