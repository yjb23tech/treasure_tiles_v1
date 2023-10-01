import random

class Player:

    def __init__(self, str_name, str_birth_place, int_age):

        self.str_name = str_name
        self.str_birth_place = str_birth_place
        self.int_age = int_age 

        self.int_atk_pwr = 1

        self.int_loc_x = 1 
        self.int_loc_y = 1
    
    def __str__(self):
        return (f"\nMy name is {self.str_name} and I'm going to be the Pirate King XD\n")

    def int_launch_atk(self):
        self.int_atk_pwr = random.randint(15,25)
        return self.int_atk_pwr 


