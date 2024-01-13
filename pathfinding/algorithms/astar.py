from typing import Callable, Type
from search_tree_pqd import SearchTreePQD
from search_node import Node
from map import Map

def construct_path(end_node: Node):
    """
    Восстанавливает маршрут, по которому пришли в заданную вершину
    """
    path = []
    cur_node = end_node
    while cur_node != None:
        path.append(cur_node)
        cur_node = cur_node.parent
    return path[::-1]

def manhattan_distance(x1, y1, x2, y2):
    return abs(int(x1)-int(x2)) + abs(int(y1)-int(y2))

def astar(map: Map, start_x, start_y, goal_x, goal_y, max_possible_traversable_difficulty=0, delta=None, heuristic_func=manhattan_distance):
    search_tree = SearchTreePQD()
    start_node = Node(start_x, start_y, g=0, h=heuristic_func(start_x, start_y, goal_x, goal_y))
    search_tree.add_to_open(start_node)

    while not search_tree.open_is_empty():
        current = search_tree.get_best_node_from_open()
        if current is None:
            break
        
        search_tree.add_to_closed(current)

        if (current.x, current.y) == (goal_x, goal_y):
            return construct_path(current)

        for neighbor_cell in map.get_neighbors_cells(current.x, current.y, max_possible_traversable_difficulty, delta):
            new_node = Node(neighbor_cell.x, neighbor_cell.y)
            if not search_tree.was_expanded(new_node):
                new_node.g = current.g + neighbor_cell.get_traversable_difficulty()
                new_node.h = heuristic_func(neighbor_cell.x, neighbor_cell.y, goal_x, goal_y)
                new_node.f = new_node.g + new_node.h
                new_node.parent = current
                search_tree.add_to_open(new_node)

    return False