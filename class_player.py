import random

class Player:

    def __init__(self, str_name):

        self.str_name = str_name
        self.int_atk_pwr = 1
        
        self.int_loc_x = 1 
        self.int_loc_y = 1
    
    def int_launch_atk(self):
        self.int_atk_pwr = random.randint(15,25)
        return self.int_atk_pwr 


