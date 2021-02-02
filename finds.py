from graph import *

def create_path(elem, ancestors):
    while elem.cell_type != START:
        elem.visited = False
        elem = ancestors[elem.id]

def BFS(graph):
    stack = list()
    ancestors = dict()

    stack.append(graph.graph[graph.start])
    graph.graph[graph.start].visited = True
    while stack:
        elem = stack.pop(0)
        if elem.cell_type == FINISH:
            create_path(elem, ancestors)
            break

        for neighbor in elem.neighbords:
            if not neighbor[0].visited:
                neighbor[0].visited = True
                ancestors[neighbor[0].id] = elem
                stack.append(neighbor[0])
        yield
    yield

def get_min(stack, costs):
    min_elem = 0
    for i in range(len(stack)):
        if costs[stack[i].id] < costs[stack[min_elem].id]:
            min_elem = i
    return stack.pop(min_elem)

def DXTR(graph):
    stack = list()
    ancestors = dict()
    costs = dict()

    stack.append(graph.graph[graph.start])
    graph.graph[graph.start].visited = True
    costs[graph.graph[graph.start].id] = 0
    while stack:
        elem = get_min(stack, costs)
        print(costs[elem.id])
        elem.visited = True

        if elem.cell_type == FINISH:
            create_path(elem, ancestors)
            break

        for neighbord in elem.neighbords:
            if (not neighbord[0].id in costs) or (costs[elem.id] + neighbord[1] < costs[neighbord[0].id]):
                ancestors[neighbord[0].id] = elem
                costs[neighbord[0].id] = costs[elem.id] + neighbord[1]
                stack.append(neighbord[0])
        yield
    yield

def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def A(graph):
    stack = list()
    ancestors = dict()
    costs = dict()

    stack.append(graph.graph[graph.start])
    graph.graph[graph.start].visited = True
    costs[graph.graph[graph.start].id] = 0
    while stack:
        elem = get_min(stack, costs)
        print(costs[elem.id])
        elem.visited = True

        if elem.cell_type == FINISH:
            create_path(elem, ancestors)
            break

        for neighbord in elem.neighbords:
            if (not neighbord[0].id in costs) or (costs[elem.id] + neighbord[1] < costs[neighbord[0].id]):
                ancestors[neighbord[0].id] = elem
                costs[neighbord[0].id] = costs[elem.id] + neighbord[1] + calc_distance(graph.graph[graph.finish].x, graph.graph[graph.finish].y, neighbord[0].x, neighbord[0].y)
                stack.append(neighbord[0])
        yield
    yield
