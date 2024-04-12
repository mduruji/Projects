import random

class model:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid_model = [[0] * width for _ in range(height)]
        self.next_grid_model = [[1] * width for _ in range(height)]
        self.cell_size = 5

        self.glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

        self.glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def randomize(self):
        import random
        for i in range(self.height):
            for j in range(self.width):
                self.grid_model[i][j] = random.randint(0, 1)

    def next_gen(self):
        for i in range(self.height):
            for j in range(self.width):
                cell = 0
                count = self.count_neighbors(i, j)

                if self.grid_model[i][j] == 0:
                    if count == 3:
                        cell = 1
                elif self.grid_model[i][j] == 1:
                    if count == 2 or count == 3:
                        cell = 1
                self.next_grid_model[i][j] = cell

        temp = self.grid_model
        self.grid_model = self.next_grid_model
        self.next_grid_model = temp

    def count_neighbors(self, row, col):
        count = 0
        if row - 1 >= 0:
            count += self.grid_model[row - 1][col]
        if (row - 1 >= 0) and (col - 1 >= 0):
            count += self.grid_model[row - 1][col - 1]
        if (row - 1 >= 0) and (col + 1 < self.width):
            count += self.grid_model[row - 1][col + 1]
        if col - 1 >= 0:
            count += self.grid_model[row][col - 1]
        if col + 1 < self.width:
            count += self.grid_model[row][col + 1]
        if row + 1 < self.height:
            count += self.grid_model[row + 1][col]
        if (row + 1 < self.height) and (col - 1 >= 0):
            count += self.grid_model[row + 1][col - 1]
        if (row + 1 < self.height) and (col + 1 < self.width):
            count += self.grid_model[row + 1][col + 1]
        return count

    def load_pattern(self, pattern, x_offset=0, y_offset=0):
        for i in range(self.height):
            for j in range(self.width):
                self.grid_model[i][j] = 0

        j = y_offset

        for row in pattern:
            i = x_offset
            for value in row:
                self.grid_model[i][j] = value
                i += 1
            j += 1


if __name__ == '__main__':
    game = model(width=100, height=100)
    game.next_gen()
