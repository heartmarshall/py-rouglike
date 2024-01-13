from map_builder import MapBuilder


class TestMapBuilder(MapBuilder):
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.walk_terrain = TerrainType(texture='.', description='Grass', traversable_difficulty=0, buff=None)
        self.fill_terrain = TerrainType(texture='#', description='Wall', traversable_difficulty=2, buff=None)
    
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

        for dx in range(-10, 10):
            for dy in range(-10, 10):
                self.map.update_cell(self.starting_point[0]-dx, self.starting_point[1]-dy, self.walk_terrain)

    def generate_bioms(self):
        pass