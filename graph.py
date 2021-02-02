import random

DEF = 3
START = 1
FINISH = 2
PATH = 4
WALL = 5

class Cell:
    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.visited = False
        self.neighbords = list()
        self.cell_type = 0
        self.rect = None

    def add_neighbord(self, neigbord):
        self.neighbords.append(neigbord)

    def set_coords(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return str(self.id)

class Graph:
    def __create_graph(self):
        graph = list()
        WALL_PRICE = 1000
        DEF_PRICE = 1

        for y in range(self.map_size):
            for x in range(self.map_size):
                nx = x + (y * self.map_size)
                new_cell = Cell()
                new_cell.cell_type = DEF if random.randint(0, 2) else WALL
                price = 0
                if x > 0:
                    if new_cell.cell_type == WALL or graph[nx - 1].cell_type == WALL:
                        price = WALL_PRICE
                    else:
                        price = DEF_PRICE
                    new_cell.add_neighbord((graph[nx - 1], price))
                    graph[nx - 1].add_neighbord((new_cell, price))
                if y > 0:
                    if new_cell.cell_type == WALL or graph[nx - self.map_size].cell_type == WALL:
                        price = WALL_PRICE
                    else:
                        price = DEF_PRICE
                    new_cell.add_neighbord((graph[nx - self.map_size], price))
                    graph[nx - self.map_size].add_neighbord((new_cell, price))
                new_cell.set_coords(y * self.cell_size, x * self.cell_size)
                new_cell.id = y * self.map_size + x
                graph.append(new_cell)
        graph[self.finish].cell_type = FINISH
        graph[self.start].cell_type = START
        return graph

    def __init__(self, map_size=10, cell_size=10):
        self.map_size = map_size
        self.cell_size = cell_size
        self.start = random.randint(0, map_size * map_size - 1)
        self.finish = random.randint(0, map_size * map_size - 1)
        self.graph = self.__create_graph()

    def __str__(self):
        response = ""
        for top in self.graph:
            response += f"id:{top.id}"
            for neighbor in top.neighbords:
                response += "-->"
                response += f"id:{neighbor.id}"
            if top.cell_type == FINISH:
                response += "\tFINISH"
            if top.cell_type == START:
                response += "\tSTART"
            response += "\n"
        return response
