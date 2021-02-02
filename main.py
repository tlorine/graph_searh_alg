from tkinter import Tk, Canvas, Frame, BOTH
from graph import *
from finds import *
import sys
import time

type_color_dict = {
    START: "#008000",
    FINISH: "#ff0000",
    DEF: "#0000ff",
    WALL: "#964b00",
    PATH: "#fff"
}

vis_color_dict = {
    START: "#004d00",
    FINISH: "#cc0000",
    DEF: "#0000cc",
    WALL: "#663300",
    PATH: "#fff"
}

funct_dict = {
    "b": BFS,
    "d": DXTR
}

class GraphVis:
    def __create_vis_graph(self):
        vis_graph = list()
        for i in self.graph.graph:
            new_rect = self.can.create_rectangle(
                i.x,
                i.y,
                i.x + self.graph.cell_size,
                i.y + self.graph.cell_size,
                fill=type_color_dict.get(i.cell_type),
                outline=vis_color_dict.get(i.visited)
            )
            i.rect = new_rect
            vis_graph.append(new_rect)
        self.can.pack(fill=BOTH, expand=1)
        return vis_graph

    def update_vis_graph(self):
        for rect in self.graph.graph:
            if rect.visited:
                color = vis_color_dict[rect.cell_type]
            else:
                color = type_color_dict[rect.cell_type]
            self.can.itemconfig(rect.rect,
                                fill=color,
                                outline=color
                                )

    def __init__(self, graph):
        self.can = Canvas()
        self.graph = graph
        self.vis_graph = self.__create_vis_graph()

def input_proccesing(argv):
    if len(argv) != 2:
        print("incorrect number of arguments: there can only be 1")
        return None
    if not argv[1] in funct_dict:
        print("wrong argument: b-BFS, d-DXTR")
        return None
    return funct_dict[argv[1]]


def main():
    func = input_proccesing(sys.argv)
    if not func:
        exit()
    window = Tk()
    window.geometry('1000x1000+0+0')
    graph = Graph(map_size=25, cell_size=25)
    vis_graph = GraphVis(graph)
    for _ in func(graph):
        vis_graph.update_vis_graph()
        window.update()
    vis_graph.update_vis_graph()
    window.mainloop()

main()