from constants import *


class Tile:
    def __init__(self, number, planets=[], wh=Wormhole.N, anomaly=Anomaly.N, base_game=True, fixed=False):
        self.number = number
        self.planets = planets
        self.anomaly = anomaly
        self.base_game = base_game
        self.fixed = fixed
        self.wormhole = wh

