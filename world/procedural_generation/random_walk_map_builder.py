from map_builder import MapBuilder
import random

class RandomWalkMapBuilder(MapBuilder):
    def __init__(self, map_width, map_height, fill_terrain: TerrainType, walk_terrain: TerrainType, number_of_paths, max_path_len):
        self.map_width = map_width
        self.map_height = map_height
        self.fill_terrain = fill_terrain
        self.walk_terrain = walk_terrain
        self.number_of_paths = number_of_paths
        self.max_path_len = max_path_len

    def init_map(self):
        if self.map_height < 10 or self.map_width < 10:
            raise ValueError("Map height and width must be greater then 10")
        self.map = Map(self.map_width, self.map_height)
        self.starting_point = (self.map_width // 2, self.map_height // 2)
    
    def generate_terrain(self):
        # Делаем заливку карты
        for y in range(self.map._height):
            for x in range(self.map._width):
                self.map.update_cell(x, y, self.fill_terrain)

        current_position = self.starting_point
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for _ in range(self.number_of_paths):
            # Выбираем случайно 3 направления из 4
            random_directions = random.sample(directions, 2)
            for _ in range(self.max_path_len):
                # Меняем направление с 30% шансом. Как показали тесты, это самый потимальный показатель
                if random.randint(0, 100) > 90:
                    random_directions = random.sample(directions, 3)
                self.map.update_cell(*current_position, self.walk_terrain)
                neighbors = self.map.get_neighbors(*current_position, max_possible_traversable_difficulty=999, delta=random_directions)
                if neighbors:
                    current_position = random.choice(neighbors)
                    if not (2 < current_position[0] < self.map_width-random.randint(1,5) and 2 < current_position[1] < self.map_height-random.randint(1,5)):
                        current_position = self.starting_point
                        break

        # Уменьшаем "шум" на карте, сглаживаем края
        for _ in range(8):
            for y in range(0, self.map._height):
                for x in range(0, self.map._width):
                    delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    window_sum = 0
                    walls_sum = 0
                    for direction in delta:
                        dx, dy = direction
                        if self.map.in_bounds(x+dx, y+dy):
                            window_sum += 1
                            if self.map.cells[y + dy][x + dx].terrain_type == self.fill_terrain:
                                walls_sum += 1
                    if walls_sum / window_sum < 0.5:
                        self.map.cells[y][x].terrain_type = self.walk_terrain

    def generate_bioms(self):
        pass