for x in range(1):
    for y in range(-1, 2):
        print(f"{x}, {y}")

print(" ")

for x in range(-1, 2):
    for y in range(1):
        print(f"{x}, {y}")

player_direction_vert = {

        0: {

            -1: '\nSouth', 
            0: 'No change', 
            1: 'North\n'
        }

}

#Who would've fucking guessed lol 
print(player_direction_vert[0][-1])
print(player_direction_vert[0][0])
print(player_direction_vert[0][1])

player_direction_horiz = {

        -1: {

            0: 'West'
        },

        0: {

            0: 'No change'
        },

        1: {

            0: 'East\n'
        }
}

print(player_direction_horiz[-1][0])
print(player_direction_horiz[0][0])
print(player_direction_horiz[1][0])



