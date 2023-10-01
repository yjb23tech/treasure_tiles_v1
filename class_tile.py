class Tile:
    
    def __init__(self, int_loc_x, int_loc_y, str_loc_quadrant, str_loc_name):

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y
        self.str_loc_quadrant = str_loc_quadrant
        self.str_loc_name = str_loc_name 
    
    def __str__(self):
        return (f"You are in the {self.str_loc_quadrant} quadrant of the map, co-ordinates [{self.int_loc_x}, {self.int_loc_y}] and have arrived at {self.str_loc_name} island\n")
    
    def pvp_tile_boss(self, player, tile_bosses):

        tile_boss = tile_bosses[self.int_loc_x][self.int_loc_y]

        while (tile_boss.int_hp > 0):

            print(f"{tile_boss.str_name} currently has a hp of {tile_boss.int_hp}!")

            tile_boss.int_hp = tile_boss.int_hp - player.int_launch_atk()
            print(f"{player.str_name} has launched a deadly attack with {player.int_atk_pwr} atk damage ")
            print(f"{tile_boss.str_name} has been wounded! They only have {tile_boss.int_hp} remaining!\n")
        
        print(f"{tile_boss.str_name} has been defeated!")
    

        

        


