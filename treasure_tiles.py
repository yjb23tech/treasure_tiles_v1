from class_player import Player
from data_structures import arr_world_map, arr_tile_bosses, arr_options 
from funcs import str_set_player_name, str_set_player_birth_place, int_set_player_age, str_welcome_msg

def play():

    bool_game_is_on = True 

    user_player = Player(str_set_player_name(), str_set_player_birth_place(), int_set_player_age())
    str_welcome_msg(user_player)

    while (bool_game_is_on == True):

        current_tile = arr_world_map[user_player.int_loc_x][user_player.int_loc_y]
        print(current_tile)

        bool_game_is_on = False

play()
    









