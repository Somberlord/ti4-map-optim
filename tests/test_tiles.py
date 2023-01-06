import random
import unittest
from mapoptim.libtiles import tiles_conf, tile as libtile

OPTIMAL_RES_AND_INF = {
    18: {'res': 0, 'inf': 6},
    19: {'res': 0, 'inf': 2},
    20: {'res': 2, 'inf': 2},
    21: {'res': 1, 'inf': 1},
    22: {'res': 1, 'inf': 1},
    23: {'res': 2, 'inf': 2},
    24: {'res': 0, 'inf': 3},
    25: {'res': 2, 'inf': 0},
    26: {'res': 3, 'inf': 0},
    27: {'res': 4, 'inf': 1},
    28: {'res': 2, 'inf': 3},
    29: {'res': 0, 'inf': 5},
    30: {'res': 3, 'inf': 2},
    31: {'res': 3, 'inf': 0},
    32: {'res': 1, 'inf': 3},
    39: {'res': 0, 'inf': 0},
    40: {'res': 0, 'inf': 0},
    41: {'res': 0, 'inf': 0},
    42: {'res': 0, 'inf': 0},
    43: {'res': 0, 'inf': 0},
    44: {'res': 0, 'inf': 0},
    45: {'res': 0, 'inf': 0},
    46: {'res': 0, 'inf': 0},
    75: {'res': 3, 'inf': 2},
    76: {'res': 1, 'inf': 4},
}


class TestTiles(unittest.TestCase):
    def test_valid_tiles(self):
        for tile in tiles_conf.TILES:
            self.assertEqual(tile, tiles_conf.TILES[tile].get_id())

    def test_optimal_res_and_ind(self):
        for tile in OPTIMAL_RES_AND_INF:
            res, inf = tiles_conf.TILES[tile].get_optimal_resource_and_influence()
            self.assertEqual(res, OPTIMAL_RES_AND_INF[tile]['res'])
            self.assertEqual(inf, OPTIMAL_RES_AND_INF[tile]['inf'])

    def test_tile_equality(self):
        tile_id = random.randrange(80)
        tile1 = libtile.Tile(tile_id)
        tile2 = libtile.Tile(tile_id)
        self.assertEqual(tile1, tile2)
