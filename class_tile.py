class Tile:
    
    def __init__(self, int_loc_x, int_loc_y, str_loc_quadrant, str_loc_name):

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y
        self.str_loc_quadrant = str_loc_quadrant
        self.str_loc_name = str_loc_name 
    
    def __str__(self):
        return (f"You are in the {self.str_loc_quadrant} quadrant of the map, co-ordinates [{self.int_loc_x}, {self.int_loc_y}] and have arrived at {self.str_loc_name} island")
    
    def pvp_tile_boss(self, tile_bosses):

        tile_boss = tile_bosses[self.int_loc_x][self.int_loc_y]
