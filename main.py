import consol_ai
import levels

level = levels.LEVELS()
def xlox():
    print("for automatic solution enter (AS)")
    way_of_playing = input("enter : ")

    print("Select Level")
    print(level.print_level())
    num_level = int(input("level : "))

    if way_of_playing == "AS" or way_of_playing == "as":
        consol_ai.start(num_level-1)
    # elif way_of_playing == "P" or way_of_playing == "p":
    #     consol_player.start(level.levels[num_level-1])

xlox()
