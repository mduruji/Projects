from tkinter import *


class GameModel:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid_model = [[0] * width for _ in range(height)]
        self.next_grid_model = [[1] * width for _ in range(height)]

        self.glider_pattern = [[0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0]]

        self.glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                                   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def count_neighbours(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= row + i < self.height and 0 <= col + j < self.width:
                    count += self.grid_model[row + i][col + j]
        return count

    def update_model(self):
        for i in range(self.height):
            for j in range(self.width):
                count = self.count_neighbours(i, j)
                if self.grid_model[i][j] == 1:
                    if count < 2 or count > 3:
                        self.next_grid_model[i][j] = 0
                else:
                    if count == 3:
                        self.next_grid_model[i][j] = 1
        self.grid_model = self.next_grid_model
        self.next_grid_model = [[0] * self.width for _ in range(self.height)]

    def set_pattern(self, pattern, start_row, start_col):
        pattern_height = len(pattern)
        pattern_width = len(pattern[0])
        for i in range(pattern_height):
            for j in range(pattern_width):
                row = (start_row + i) % self.height
                col = (start_col + j) % self.width
                self.grid_model[row][col] = pattern[i][j]


class GameView:
    def __init__(self, master, height, width, cell_size):
        self.master = master
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.canvas = Canvas(self.master, width=self.width * self.cell_size,
                             height=self.height * self.cell_size, bg='white')
        self.canvas.pack()

    def draw_grid(self, model):
        self.canvas.delete('cells')
        for i in range(model.height):
            for j in range(model.width):
                if model.grid_model[i][j] == 1:
                    x1 = j * self.cell_size
                    y1 = i * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='black', tags='cells')

    def start_animation(self, model, delay):
        model.update_model()
        self.draw_grid(model)
        self.master.after(delay, self.start_animation, model, delay)


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_click(self, event):
        row = event.y // self.view.cell_size
        col = event.x // self.view.cell_size
        self.model.grid_model[row][col] = 1
        self.view.draw_grid(self.model)

    def handle_keypress(self, event):
        if event.char == 'q':
            self.view.master.destroy()
        elif event.char == 'g':
            self.model.set_pattern(self.model.glider_pattern, 1, 1)
            self.view.draw_grid(self.model)
        elif event.char == 'p':
            self.model.set_pattern(self.model.glider_gun_pattern, 1, 1)
            self.view.draw_grid(self.model)

    def start(self):
        self.view.draw_grid(self.model)
        self.view.canvas.bind('<Button-1>', self.handle_click)
        self.view.master.bind('<KeyPress>', self.handle_keypress)
        self.view.start_animation(self.model, 100)


def main():
    root = Tk()
    root.title("Game of Life")
    height = 40
    width = 0
    cell_size = 15

    model = GameModel(height, width)
    view = GameView(root, height, width, cell_size)
    controller = GameController(model, view)

    controller.start()

    root.mainloop()


if __name__ == '__main__':
    main()
