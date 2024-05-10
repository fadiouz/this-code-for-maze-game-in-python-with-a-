class FUNCTION:

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
        print(cells)
        for cell in range(len(cells)):
            x = cells[cell][0]
            y = cells[cell][1]

            for cell in cells:
                if first_patch[cell[0]][cell[1]] == "1":
                    first_patch[cell[0]][cell[1]] = "#"

        self.print_single_patch(first_patch)
        print("Solution Depth : ", solution_depth)
        print("Visited Node : ", visited_node)


