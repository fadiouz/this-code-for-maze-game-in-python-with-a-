class FUNCTION:
    def number_of_white_cell(self, patch):
        number_of_white_cell = 0
        for row in range(1, len(patch) - 1):
            for col in range(1, len(patch[0]) - 1):
                if patch[row][col] == "1":
                    number_of_white_cell += 1
        return number_of_white_cell

    def number_of_black_cell(self, patch):
        number_of_white_cell = 0
        for row in range(1, len(patch) - 1):
            for col in range(1, len(patch[0]) - 1):
                if patch[row][col] == "B":
                    number_of_white_cell += 1
        return number_of_white_cell

    def print_patchs(self, patchs):
        for patch in patchs:
            numRows = len(patch)
            numCols = len(patch[0])
            i = 0

            #print number of col
            for j in range(numCols):
                if j == 0:
                    print("    ", j, end="  ")
                else:
                    print(j, end="  ")
            print()

            for row in patch:
                #print number of row
                print(i,"|", end="  ")
                i+=1
                for cell in row:
                    #print patch
                    print(cell, end="  ")
                print()
            print("--------------------------------")

    # def print_solution2(self):


    def get_value_of_cell(self, patch, cell):
        cell_value = patch[cell[0]][cell[1]]
        return cell_value

    def find_goal_coordinates(self, patch):
        for row in range(0, len(patch)):
            for col in range(0, len(patch[0])):
                if patch[row][col] == "2":
                    return (row, col)

    def find_start_coordinates(self, patch):
        all_start_coordinates = set()

        for row in range(1):
            for col in range(len(patch[0])):
                if patch[row][col] == "1":
                    all_start_coordinates.add((row, col))

        for col in range(1):
            for row in range(len(patch)):
                if patch[row][col] == "1":
                    all_start_coordinates.add((row, col))

        return list(all_start_coordinates)

    def print_single_patch(self, patch):
        # numRows = len(patch)
        numCols = int(len(patch[0]))
        i = 0

        # print number of col
        for j in range(numCols):
            if j == 0:
                print("    ", j, end="  ")
            else:
                print(j, end="  ")
        print()

        for row in patch:
            # print number of row
            print(i, "|", end="  ")
            i += 1
            for cell in row:
                # print patch
                print(cell, end="  ")
            print()

    def print_solution(self, first_patch, cells, visited_node):
        solution_depth = len(cells)
        print("Path Solution :")
        self.print_single_patch(first_patch)
        for cell in range(len(cells)):
            x = cells[cell][0]
            y = cells[cell][1]
            if (first_patch[x][y] == 'W'):

                first_patch[x][y] = "B"

                patch_list = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
                for cell in patch_list:
                    if first_patch[cell[0]][cell[1]] == "B":
                        first_patch[cell[0]][cell[1]] = "W"

                    elif first_patch[cell[0]][cell[1]] == "W":
                        first_patch[cell[0]][cell[1]] = "B"
                    else:
                        first_patch[cell[0]][cell[1]] = first_patch[cell[0]][cell[1]]
                print((x,y))
                self.print_single_patch(first_patch)
        print("Solution Depth : ", solution_depth)
        print("Visited Node : ", visited_node+1)

    def num_white_black_block(self, patch, x, y):
        cost = 0
        patch_list = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for cell in patch_list:
            if patch[cell[0]][cell[1]] == "B":
                cost += 2

            elif patch[cell[0]][cell[1]] == "W":
                cost += 1

            else:
                cost += 0

        return cost

    def num_white_near(self, patch, x, y):
        cost = 0
        patch_list = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for cell in patch_list:
            if patch[cell[0]][cell[1]] == "W":
                cost += 1

        return cost

    def num_cell_chang_color(self, patch, x, y):
        cost = 1
        patch_list = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for cell in patch_list:
            if patch[cell[0]][cell[1]] == "W" or patch[cell[0]][cell[1]] == "B":
                cost += 1
        return cost

    def num_row_contain_cell_white(self, patch):
        number_of_white_cell = 0
        for row in range(1, len(patch) - 1):
            for col in range(1, len(patch[0]) - 1):
                if patch[row][col] == "W":
                    number_of_white_cell += 1
                    continue
        return number_of_white_cell

    def num_blocks(self, patch):
        number = 0
        for row in range(1, len(patch) - 1):
            for col in range(1, len(patch[0]) - 1):
                if patch[row][col] == "W":
                    if patch[row][col + 1] != "B" and patch[row][col - 1] != "B" and patch[row + 1][col] != "B" and patch[row - 1][col] != "B":
                        number += 1
        return number

