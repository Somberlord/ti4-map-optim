import unittest
from mapoptim.libtiles import slice, tile


class TestSlices(unittest.TestCase):
    def test_slice_builder(self):
        test_slice = slice.Slice2Rings()
        test_slice.load_standard_slice(left_home=tile.Tile(1),
                                       right_home=tile.Tile(2),
                                       front_home=tile.Tile(3),
                                       left_eq=tile.Tile(4),
                                       adj_mec=tile.Tile(5))
        test_slice_dict = test_slice.get_standard_slice_dict()
        self.assertEqual(test_slice_dict[slice.Slice.LH], tile.Tile(1))
        self.assertEqual(test_slice_dict[slice.Slice.RH], tile.Tile(2))
        self.assertEqual(test_slice_dict[slice.Slice.FH], tile.Tile(3))
        self.assertEqual(test_slice_dict[slice.Slice.LE], tile.Tile(4))
        self.assertEqual(test_slice_dict[slice.Slice.AM], tile.Tile(5))

    def test_from_string(self):
        slice_string = "21,66,69,40,80"
        test_slice = slice.Slice2Rings()
        test_slice.load_from_string(slice_string)
        self.assertEqual(test_slice.left_home, tile.Tile(21))
        self.assertEqual(test_slice.front_home, tile.Tile(66))
        self.assertEqual(test_slice.right_home, tile.Tile(69))
        self.assertEqual(test_slice.left_equidistant, tile.Tile(40))
        self.assertEqual(test_slice.adj_mecatol, tile.Tile(80))
        slice_string = "21 66 69 40 80"
        test_slice = slice.Slice2Rings()
        test_slice.load_from_string(slice_string)
        self.assertEqual(test_slice.left_home, tile.Tile(21))
        self.assertEqual(test_slice.front_home, tile.Tile(66))
        self.assertEqual(test_slice.right_home, tile.Tile(69))
        self.assertEqual(test_slice.left_equidistant, tile.Tile(40))
        self.assertEqual(test_slice.adj_mecatol, tile.Tile(80))
