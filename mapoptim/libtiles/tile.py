from .constants import *


class Tile:
    def __init__(self, number, planets=[], wh=Wormhole.N, anomaly=Anomaly.N, base_game=True, fixed=False):
        self.__id = number
        self.__planets = planets
        self.anomaly = anomaly
        self.base_game = base_game
        self.fixed = fixed
        self.wormhole = wh

    def __eq__(self, other):
        return self.__id == other.__id

    def get_id(self):
        return self.__id

    def get_optimal_resource_and_influence(self):
        res, inf = 0, 0
        for planet in self.__planets:
            pres, pinf = planet.get_resource_and_influence()
            if pres > pinf:
                pinf = 0
            elif pinf > pres:
                pres = 0
            res += pres
            inf += pinf
        return res, inf

