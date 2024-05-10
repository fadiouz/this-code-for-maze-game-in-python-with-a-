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


def astar(patch):
    global goal_coordinates, index
    goal_coordinates = fun.find_goal_coordinates(patch)

    start_coordinates = fun.find_start_coordinates(patch)
    for x in start_coordinates:
        result = (x[0] - goal_coordinates[0]) + (x[1] - goal_coordinates[1])
        heapq.heappush(priority_queue, (
        abs(result), index, {"patch": patch, "index": index, "cost": abs(result), "parent": 'none', "cell": x, "steps": 0}))
        node[index] = {"patch": patch, "index": index, "cost": abs(result), "parent": 'none', "cell": x, "steps": 0}
        index += 1
    print(priority_queue)
    is_visit()

def is_visit():
    while priority_queue:

        _, _, item = heapq.heappop(priority_queue)

        if (item['cell'], item['parent']) in visited:
            continue

        visited[item['cell'], item['parent']] = {"index": item['index'], "cost": item['cost'], "cell": item['cell'], "parent": item['parent']}

        test(item)

def test(item):
    cells_solution = []
    cell_value = fun.get_value_of_cell(item["patch"], item["cell"])

    if cell_value == "2":
        fa = item["parent"]

        while fa != "none":
            cell = node[fa]['cell']
            cells_solution.append(cell)
            fa = node[fa]["parent"]

        reversed_cells_solution = list(reversed(cells_solution))

        # reversed_cells_solution.remove("none")
        reversed_cells_solution.append(item["cell"])
        print(reversed_cells_solution)
        # visited_node = len(visited)
        # print(visited_node)
        # generated_nodes = len(visited) + len(priority_queue)
        # fun.print_solution2(first_patch, reversed_cells_solution)
        # print('Generated Nodes : ', generated_nodes)
        print("The End")

        return exit()
    else:

        get_child(item)

def get_child(item):
    global index, parent
    patch = item["patch"]
    parent = item["index"]
    step = item["steps"] + 1
    old_cost = item['cost']
    row = item['cell'][0]
    col = item['cell'][1]

    patch_list = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]


    for x in patch_list:
        index += 1
        if fun.get_value_of_cell(patch, x) == "1" or fun.get_value_of_cell(patch, x) == "2":

            result = (x[0] - goal_coordinates[0]) + (x[1] - goal_coordinates[1])
            heapq.heappush(priority_queue, (
                abs(result), index,
                {"patch": patch, "index": index, "cost": abs(result)+index, "parent": parent, "cell": x, "steps": step}))
            node[index] = {"patch": patch, "index": index, "cost": abs(result)+index, "parent": parent, "cell": x, "steps": step}


    # for row in range(0, len(patch)):
    #     for col in range(0, len(patch[0])):
    #         if patch[row][col] == "1":
    #             childs.append((row, col))
    # for child in range(len(childs)):
    #     x = childs[child][0]
    #     y = childs[child][1]
    #
    #     new_patch = [row[:] for row in patch]
    #     if new_patch[x][y] == '1':
    #         # new_patch[x][y] = "B"
    #
    #         patch_list = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    #         for cell in patch_list:
    #             if new_patch[cell[0]][cell[1]] == "B":
    #                 new_patch[cell[0]][cell[1]] = "W"
    #
    #             elif new_patch[cell[0]][cell[1]] == "W":
    #                 new_patch[cell[0]][cell[1]] = "B"
    #             else:
    #                 new_patch[cell[0]][cell[1]] = patch[cell[0]][cell[1]]
    #
    #         num_white = fun.number_of_white_cell(new_patch)
    #         num_white_black_block = fun.num_white_black_block(new_patch, x, y)
    #
    #         cost = num_white + num_white_black_block
    #         index += 1
    #
    #         hash_patch = hash(str(new_patch))
    #
    #         if not hash_patch in visited:
    #             heapq.heappush(priority_queue, (cost, index, {"patch": new_patch, "index": index, "cost": cost, "parent": parent,
    #                                              "cell": (x, y), "steps": step}))
    #             heapq.heapify(priority_queue)
    #
    #             node[index] = {"patch": new_patch, "index": index, "cost": cost, "parent": parent, "cell": (x,y),"hash": hash_patch, "steps": step}
    #         else:
    #             old_cost = visited[hash_patch]["cost"]
    #             del visited[hash_patch]
    #
    #             if cost < old_cost:
    #                 heapq.heappush(priority_queue, (cost, index,{"patch": new_patch, "index": index, "cost": cost, "parent": parent,
    #                                                  "cell": (x, y), "steps": step}))
    #                 heapq.heapify(priority_queue)
    #
    #                 node[index] = {"patch": new_patch, "index": index, "cost": cost, "parent": parent, "cell": (x, y),
    #                                "hash": hash_patch, "steps": step}

    is_visit()

def start_game_astar(patch):
    global first_patch
    first_patch = patch
    fun.print_single_patch(patch)

    astar(patch)


