class Foe:

    def __init__(self, str_name, str_devil_fruit):

        self.str_name = str_name
        self.str_devil_fruit = str_devil_fruit
        self.int_hp = 50 
    
    def __str__(self):
        return (f"I am {self.str_name}! Prepare for battle against my deadly fruit the {self.str_devil_fruit} fruit")

