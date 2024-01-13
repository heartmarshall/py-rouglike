from typing import List, Tuple
from cell import Cell
from point import Point


class Map:
    def __init__(self, width, height) -> None:
        self.cells = [[None for i in range(width)] for j in range(height)]
        self._width = width
        self._height = height

    def inBounds(self, x: int, y: int) -> bool:
        return 0 <= x < self._width and 0 <= y < self._height
    
    def traversableDifficulty(self, x: int, y: int) -> bool:
        """
        Возвращает сложность проходимости клектки по координатам x, y
        """
        return self.cells[y][x].get_traversable_difficulty()
    
    def set_cell(self, x, y, terrain_type, items=None, occupied_by=None):
        """
        Перезаписсывает параметры клетки по координатам x, y
        """
        cell = Cell(x, y, terrain_type, items, occupied_by)
        self.cells[y][x] = cell
        return cell
    
    def cellInfo(self, x:int, y:int) -> Cell:
        """
        Возвращает клетку (Cell), находящуюся на карте по координатам x, y

        Params:
        x,y:int: координаты точки, для которой нужно получить клетку

        Return:
        Объект класса Cell, который находится на карте по координатам x, y
        """
        return self.cells[y][x]
    
    def getNeighbors(self, x: int, y: int, max_possible_traversable_difficulty=0, delta=None) -> List[Tuple[int, int]]:
        """
        Возвращает координаты клеток, в которые можно попасть из заданной, учитывая максимальную возможную проходимость и доступные переходы.

        Params:
        x,y:int: координаты точки, для которой нужно найти соседей.
        max_possible_traversable_difficulty:int: максимальная проходимость.
        delta:List[int]: список переходов, для которых нужно узнать, возможны ли они. По-умолчанию это переходы 4-х связанного грида: N, W, S, E

        Return:
        Список из точек (класса Point), в которые можно попасть: [Point(x1, y1), Point(x2, y2), ...]

        Пример использования:
        Если мы хотим узнать какие клетки доступны при передвижении по типу шахматного коня, то вызов методы будет следующим:
        .get_neighbours(0, 0, delta=((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
        """
        neighbors = []
        if delta == None:
            delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if self.inBounds(nx, ny) and self.traversableDifficulty(nx, ny) <= max_possible_traversable_difficulty:
                neighbors.append(Point(nx, ny))
        return neighbors

    def getSize(self) -> Tuple[int, int]:
        return self._height, self._width