
import Game_AI_A_STAR
import levels

level = levels.LEVELS()

def start(num_level):
    algorithm = input("(for A* select 'A') : ")
    if algorithm == "A" or algorithm == "a":
        Game_AI_A_STAR.start_game_astar(level.levels[num_level])
