from tile import Tile
from planet import Planet
from constants import *

TILES = {
    # Base Game
    18: Tile(18, planets=[Planet('Mecatol Rex', 1, 6)], fixed=True),
    19: Tile(19, planets=[Planet('Wellon', 1, 2, traits=Trait.IND, skips=Skip.Y)]),
    20: Tile(20, planets=[Planet('Vefut II', 2, 2, traits=Trait.HAZ)]),
    21: Tile(20, planets=[Planet('Thibah', 1, 1, traits=Trait.IND, skips=Skip.B)]),
    22: Tile(22, planets=[Planet("Tar'mann", 1, 1, traits=Trait.IND, skips=Skip.G)]),
    23: Tile(23, planets=[Planet("Saudor", 2, 2, traits=Trait.IND)]),
    24: Tile(24, planets=[Planet("Mehar Xull", 1, 3, traits=Trait.HAZ, skips=Skip.B)]),
    25: Tile(25, planets=[Planet("Quann", 2, 1, traits=Trait.CUL)], wh=Wormhole.B),
    26: Tile(26, planets=[Planet("Lodor", 3, 1, traits=Trait.CUL)], wh=Wormhole.A),
    27: Tile(27, planets=[Planet("New albion", 1, 1, traits=Trait.IND, skips=Skip.G),
                          Planet("Starpoint", 3, 1, traits=Trait.HAZ)]),
    28: Tile(28, planets=[Planet("Taqu'ran", 2, 0, traits=Trait.HAZ),
                          Planet("Torkan", 0, 3, traits=Trait.CUL)]),
    29: Tile(29, planets=[Planet("Qucen'n", 1, 2, traits=Trait.IND),
                          Planet("Rarron", 0, 3, traits=Trait.CUL)]),
    30: Tile(30, planets=[Planet("Mellon", 0, 2, traits=Trait.CUL),
                          Planet("Zohbat", 3, 1, traits=Trait.HAZ)]),
    31: Tile(31, planets=[Planet("Lazar", 1, 0, traits=Trait.IND, skips=Skip.Y),
                          Planet("Sakulag", 2, 1, traits=Trait.HAZ)]),
    32: Tile(32, planets=[Planet("Dal Bootha", 0, 2, traits=Trait.CUL,),
                          Planet("Xxehan", 1, 1, traits=Trait.CUL)]),
    33: Tile(33, planets=[Planet("Corneeq", 1, 2, traits=Trait.CUL,),
                          Planet("Resculon", 2, 0, traits=Trait.CUL)]),
    34: Tile(34, planets=[Planet("Centauri", 1, 3, traits=Trait.CUL,),
                          Planet("Gral", 1, 1, traits=Trait.IND, skips=Skip.B)]),
    35: Tile(35, planets=[Planet("Bereg", 3, 1, traits=Trait.HAZ,),
                          Planet("Lirta IV", 2, 3, traits=Trait.HAZ)]),
    36: Tile(36, planets=[Planet("Arnor", 2, 1, traits=Trait.IND,),
                          Planet("Lor", 1, 2, traits=Trait.IND)]),
    37: Tile(37, planets=[Planet("Arinam", 1, 2, traits=Trait.IND,),
                          Planet("Meer", 0, 4, traits=Trait.HAZ, skips=Skip.R)]),
    38: Tile(38, planets=[Planet("Abyz", 3, 0, traits=Trait.HAZ,),
                          Planet("Fria", 2, 0, traits=Trait.HAZ)]),
    39: Tile(39, wh=Wormhole.A),
    40: Tile(40, wh=Wormhole.B),
    41: Tile(41, anomaly=Anomaly.GRR),
    42: Tile(42, anomaly=Anomaly.NEB),
    43: Tile(43, anomaly=Anomaly.SUP),
    44: Tile(44, anomaly=Anomaly.ASF),
    45: Tile(45, anomaly=Anomaly.ASF),
    46: Tile(46),
    47: Tile(47),
    48: Tile(48),
    49: Tile(49),
    50: Tile(50),
    # PoK
    59: Tile(59, base_game=False, planets=[Planet("Archon Vail", 1, 3, traits=Trait.HAZ, skips=Skip.B)]),
    60: Tile(60, base_game=False, planets=[Planet("Perimeter", 2, 1, traits=Trait.IND)]),
    61: Tile(61, base_game=False, planets=[Planet("Ang", 2, 0, traits=Trait.IND, skips=Skip.R)]),
    62: Tile(62, base_game=False, planets=[Planet("Sem-Lore", 3, 2, traits=Trait.CUL, skips=Skip.Y)]),
    63: Tile(63, base_game=False, planets=[Planet("Vorhal", 2, 0, traits=Trait.CUL, skips=Skip.G)]),
    64: Tile(64, base_game=False, planets=[Planet("Atlas", 3, 1, traits=Trait.HAZ)]),
    65: Tile(65, base_game=False, planets=[Planet("Primor", 2, 1, traits=Trait.CUL, legendary=True)]),
    66: Tile(66, base_game=False, planets=[Planet("Hope's End", 3, 0, traits=Trait.HAZ, legendary=True)]),
    67: Tile(67, base_game=False, planets=[Planet("Cormud", 2, 0, traits=Trait.HAZ)], anomaly=Anomaly.GRR),
    68: Tile(68, base_game=False, planets=[Planet("Everra", 3, 1, traits=Trait.CUL)], anomaly=Anomaly.NEB),
    69: Tile(69, base_game=False, planets=[Planet("Accoen", 2, 3, traits=Trait.IND),
                                           Planet("Jeol Ir", 2, 3, traits=Trait.IND)]),
    70: Tile(70, base_game=False, planets=[Planet("Kraag", 2, 1, traits=Trait.HAZ),
                                           Planet("Siig", 0, 2, traits=Trait.HAZ)]),
    71: Tile(71, base_game=False, planets=[Planet("Ba'kal", 3, 2, traits=Trait.IND),
                                           Planet("Alio Prima", 1, 1, traits=Trait.CUL)]),
    72: Tile(72, base_game=False, planets=[Planet("Lisis", 2, 2, traits=Trait.IND),
                                           Planet("Velnor", 2, 1, traits=Trait.IND, skips=Skip.R)]),
    73: Tile(73, base_game=False, planets=[Planet("Cealdri", 0, 2, traits=Trait.CUL, skips=Skip.Y),
                                           Planet("Xanhact", 0, 1, traits=Trait.HAZ)]),
    74: Tile(74, base_game=False, planets=[Planet("Vega Major", 2, 1, traits=Trait.CUL),
                                           Planet("Vega Minor", 1, 2, traits=Trait.CUL, skips=Skip.B)]),
    75: Tile(75, base_game=False, planets=[Planet("Loki", 1, 2, traits=Trait.CUL),
                                           Planet("Abaddon", 1, 0, traits=Trait.CUL),
                                           Planet("Ashtroth", 2, 0, traits=Trait.HAZ)]),
    76: Tile(76, base_game=False, planets=[Planet("Rigel III", 1, 1, traits=Trait.IND, skips=Skip.G),
                                           Planet("Rigel II", 1, 2, traits=Trait.IND),
                                           Planet("Rigel I", 0, 1, traits=Trait.HAZ)]),
    77: Tile(77, base_game=False),
    78: Tile(78, base_game=False),
    79: Tile(79, base_game=False, anomaly=Anomaly.ASF, wh=Wormhole.A),
    80: Tile(80, base_game=False, anomaly=Anomaly.SUP),
}
