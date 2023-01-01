from constants import *


class Planet:
    def __init__(self, name, r, i, traits=Trait.NONE, skips=Skip.N, legendary=False):
        self.name = name
        self.resources = r
        self.influence = i
        self.traits = traits
        self.skips = skips
        self.legendary = legendary
