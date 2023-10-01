for x in range(len(arr_world_map)):
    for y in range(len(arr_world_map)):
        print(arr_world_map[x][y])
    print(" ")


for x in range(len(arr_tile_bosses)):
    for y in range(len(arr_tile_bosses)):
        print(arr_tile_bosses[x][y])
    print(" ")

test_player = Player("Yuri Orlov")

valid_tile = arr_world_map[0][0]
valid_tile.pvp_tile_boss(test_player, arr_tile_bosses)

