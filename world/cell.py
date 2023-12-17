class Cell:
    def __init__(self, x, y, terrain_type, items=None, occupied_by=None):
        self.x = x
        self.y = y
        self.terrain_type = terrain_type
        self.items = items or []
        self.occupied_by = occupied_by

    def get_traversable_difficulty(self):
        return self.terrain_type.traversable_difficulty