import heapq
import sys
import functions

index = 0
visited = {}
node = {}
priority_queue = []
parent = 0
fun = functions.FUNCTION()
sys.setrecursionlimit(10000)
first_patch = []


def astar(cell):
    global goal_coordinates

    goal_coordinates = fun.find_goal_coordinates(first_patch)

    result = (cell[0] - goal_coordinates[0]) + (cell[1] - goal_coordinates[1])
    heapq.heappush(priority_queue, (
    abs(result), index, {"index": index, "cost": abs(result), "parent": 'none', "cell": cell, "steps": 0}))
    node[index] = {"index": index, "cost": abs(result), "parent": 'none', "cell": cell, "steps": 0}
    is_visit()

def is_visit():
    while priority_queue:

        _, _, item = heapq.heappop(priority_queue)

        if (item['cell']) in visited:
            continue

        visited[item['cell']] = {"index": item['index'], "cost": item['cost'], "cell": item['cell'], "parent": item['parent']}

        test(item)

def test(item):
    cells_solution = []
    cell_value = fun.get_value_of_cell(first_patch, item["cell"])

    if cell_value == "2":
        fa = item["parent"]

        while fa != "none":
            cell = node[fa]['cell']
            cells_solution.append(cell)
            fa = node[fa]["parent"]

        reversed_cells_solution = list(reversed(cells_solution))
        reversed_cells_solution.append(item["cell"])
        visited_node = len(visited)
        fun.print_solution(first_patch, reversed_cells_solution, visited_node)
        print("The End")

        return exit()
    else:

        get_child(item)

def get_child(item):
    global index, parent
    parent = item["index"]
    step = item["steps"] + 1
    row = item['cell'][0]
    col = item['cell'][1]
    patch_list = []

    if col + 1 < len(first_patch[0]) and col + 1 >= 0:
        patch_list.append((row, col + 1))

    if col - 1 < len(first_patch[0]) and col - 1 >= 0:
        patch_list.append((row, col - 1))

    if row + 1 < len(first_patch) and row + 1 >= 0:
        patch_list.append((row + 1, col))

    if row - 1 < len(first_patch) and row - 1 >= 0:
        patch_list.append((row - 1, col))


    for x in patch_list:
        index += 1
        if fun.get_value_of_cell(first_patch, x) == "1" or fun.get_value_of_cell(first_patch, x) == "2":

            result = abs(x[0] - goal_coordinates[0]) + abs(x[1] - goal_coordinates[1])
            heapq.heappush(priority_queue, (
                abs(result), index,
                {"index": index, "cost": abs(result), "parent": parent, "cell": x, "steps": step}))

            node[index] = {"index": index, "cost": abs(result), "parent": parent, "cell": x, "steps": step}

    is_visit()

def start_game_astar(patch):
    global first_patch
    first_patch = patch
    fun.print_single_patch(patch)
    print('enter point start')
    x_point_start = input("enter row: ")
    y_point_start = input("enter col: ")
    x_point_start = int(x_point_start)
    y_point_start = int(y_point_start)
    cell = (x_point_start, y_point_start)

    if first_patch[x_point_start][y_point_start] == "1":
        astar(cell)
    else:
        print("this point cant you selected")


