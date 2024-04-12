from tkinter import *


class GameOfLife:
    def __init__(self):
        self.cell_size = 5
        self.is_running = False
        self.root = None
        self.grid_view = None
        self.start_button = None
        self.clear_button = None
        self.choice = None
        self.width = 0
        self.height = 0
        self.grid_model = []
        self.next_grid_model = []

    def setup(self):
        self.root = Tk()
        self.root.title('The Game of Life')

        self.grid_view = Canvas(
            self.root,
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
            borderwidth=0,
            highlightthickness=0,
            bg='white'
        )

        self.start_button = Button(self.root, text='Start', width=12)
        self.clear_button = Button(self.root, text='Clear', width=12)

        self.choice = StringVar(self.root)
        self.choice.set('Choose a Pattern')
        option = OptionMenu(
            self.root,
            self.choice,
            'Choose a Pattern',
            'glider',
            'glider gun',
            'random',
            command=self.option_handler
        )
        option.config(width=20)

        self.grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
        self.grid_view.bind('<Button-1>', self.grid_handler)
        self.start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
        self.start_button.bind('<Button-1>', self.start_handler)
        option.grid(row=1, column=1, padx=20)
        self.clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)
        self.clear_button.bind('<Button-1>', self.clear_handler)

    def option_handler(self, event):
        self.is_running = False
        self.start_button.configure(text='Start')

        selection = self.choice.get()

        if selection == 'glider':
            self.load_pattern(self.glider_pattern, 10, 10)
        elif selection == 'glider gun':
            self.load_pattern(self.glider_gun_pattern, 10, 10)
        elif selection == 'random':
            self.randomize(self.grid_model, self.width, self.height)

        self.update()

    def start_handler(self, event):
        if self.is_running:
            self.is_running = False
            self.start_button.configure(text='Start')
        else:
            self.is_running = True
            self.start_button.configure(text='Pause')
            self.update()

    def clear_handler(self, event):
        self.is_running = False
        for i in range(self.height):
            for j in range(self.width):
                self.grid_model[i][j] = 0

        self.start_button.configure(text='Start')
        self.update()

    def grid_handler(self, event):
        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)

        if self.grid_model[y][x] == 1:
            self.grid_model[y][x] = 0
            self.draw_cell(x, y, 'white')
        else:
            self.grid_model[y][x] = 1
            self.draw_cell(x, y, 'black')

    def update(self):
        self.grid_view.delete(ALL)

        self.next_gen()
        for i in range(self.height):
            for j in range(self.width):
                if self.grid_model[i][j] == 1:
                    self.draw_cell(j, i, 'black')

        if self.is_running:
            self.root.after(100, self.update)

    def draw_cell(self, x, y, color):
        x1 = x * self.cell_size
        y1 = y * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.grid_view.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def load_pattern(self, pattern, start_x, start_y):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                self.grid_model[start_y + i][start_x + j] = pattern[i][j]

    def randomize(self, grid, width, height):
        import random
        for i in range(height):
            for j in range(width):
                grid[i][j] = random.randint(0, 1)

    def next_gen(self):
        for i in range(self.height):
            for j in range(self.width):
                cell_state = self.grid_model[i][j]
                live_neighbors = self.count_live_neighbors(i, j)

                if cell_state == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        self.next_grid_model[i][j] = 0
                    else:
                        self.next_grid_model[i][j] = 1
                else:
                    if live_neighbors == 3:
                        self.next_grid_model[i][j] = 1
                    else:
                        self.next_grid_model[i][j] = 0

        self.grid_model, self.next_grid_model = self.next_grid_model, self.grid_model

    def count_live_neighbors(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_row = (row + i + self.height) % self.height
                neighbor_col = (col + j + self.width) % self.width
                count += self.grid_model[neighbor_row][neighbor_col]
        count -= self.grid_model[row][col]
        return count

    def run(self, width, height):
        self.width = width
        self.height = height
        self.grid_model = [[0] * self.width for _ in range(self.height)]
        self.next_grid_model = [[0] * self.width for _ in range(self.height)]

        self.setup()
        self.root.mainloop()


if __name__ == '__main__':
    model = GameOfLife()
    model.run(width=100, height=100)
