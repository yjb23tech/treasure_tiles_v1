def str_set_player_name() -> str:

    ui_player_name = input("\nWhat is your name Sailor?\n")
    return ui_player_name

def str_set_player_birth_place() -> str:

    ui_player_birth_place = input("\nWhere ye be born from Sailor?\n")
    return ui_player_birth_place

def int_set_player_age() -> int:

    ui_player_age = int(input("\nAnd how old ye be Sailor?\n"))
    return ui_player_age

def str_welcome_msg(player):
    print(f"\nWelcome {player.str_name}! Who would've thought a wee sappling from {player.str_birth_place} would brave the 7 seas!\n")

