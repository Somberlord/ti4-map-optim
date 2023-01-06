
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
        self.__home_system = None
        self.__left_home = None
        self.__right_home = None
        self.__front_home = None
        self.__left_equidistant = None
        self.__right_equidistant = None
        self.__adj_mecatol = None

    def get_slice_dict(self):
        pass


class Slice2Rings(Slice):
    def __init__(self):
        Slice.__init__(self, 2)

    def load_standard_slice(self, left_home=None, right_home=None, front_home=None, left_eq=None, adj_mec=None):
        self.__left_home = left_home
        self.__right_home = right_home
        self.__front_home = front_home
        self.__left_equidistant = left_eq
        self.__adj_mecatol = adj_mec

    def get_standard_slice_dict(self):
        return {
            Slice.LH: self.__left_home,
            Slice.RH: self.__right_home,
            Slice.FH: self.__front_home,
            Slice.LE: self.__left_equidistant,
            Slice.AM: self.__adj_mecatol,
        }
    