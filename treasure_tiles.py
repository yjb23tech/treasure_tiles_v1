from class_player import Player
from data_structures import arr_world_map, arr_tile_bosses

test_player = Player("Yuri Orlov")

valid_tile = arr_world_map[0][0]
valid_tile.pvp_tile_boss(test_player, arr_tile_bosses)


