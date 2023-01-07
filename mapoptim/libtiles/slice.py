import re
from .tiles_conf import TILES


class Slice:
    HS = "home_system"
    LH = "left_home"
    RH = "right_home"
    FH = "front_home"
    LE = "left_equidistant"
    RE = "right_equidistant"
    AM = "adjacent_mecatol"

    def __init__(self, rings=2):
        assert(rings == 2 or rings == 3)
        self.home_system = None
        self.left_home = None
        self.right_home = None
        self.front_home = None
        self.left_equidistant = None
        self.right_equidistant = None
        self.adj_mecatol = None

    def get_slice_dict(self):
        pass


class Slice2Rings(Slice):
    def __init__(self):
        Slice.__init__(self, 2)

    def load_standard_slice(self, left_home=None, right_home=None, front_home=None, left_eq=None, adj_mec=None):
        self.left_home = left_home
        self.right_home = right_home
        self.front_home = front_home
        self.left_equidistant = left_eq
        self.adj_mecatol = adj_mec

    def get_standard_slice_dict(self):
        return {
            Slice.LH: self.left_home,
            Slice.RH: self.right_home,
            Slice.FH: self.front_home,
            Slice.LE: self.left_equidistant,
            Slice.AM: self.adj_mecatol,
        }

    def load_from_string(self, in_string):
        pattern = re.compile("([0-9]{2})[^0-9]([0-9]{2})[^0-9]([0-9]{2})[^0-9]([0-9]{2})[^0-9]([0-9]{2})")
        match = pattern.fullmatch(in_string)
        if match is not None:
            self.left_home = TILES[int(match.group(1))]
            self.front_home = TILES[int(match.group(2))]
            self.right_home = TILES[int(match.group(3))]
            self.left_equidistant = TILES[int(match.group(4))]
            self.adj_mecatol = TILES[int(match.group(5))]
        else:
            raise ValueError('Unexpected slice string '+in_string)
