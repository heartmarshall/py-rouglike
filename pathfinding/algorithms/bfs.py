from collections import deque
from search_node import Node


def bfs(map, start_x, start_y, max_possible_traversable_difficulty=0, delta=None):
    start_node = (start_x, start_y)
    visited = {(start_node)}
    queue = deque([start_node])
    while len(queue) != 0:
        curr_vert = queue.popleft()
        for neighbor in map.get_neighbors(curr_vert[0], curr_vert[1], max_possible_traversable_difficulty, delta):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return visited