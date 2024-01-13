class Terrain:
    def __init__(self, texture, description="No description", traversable_difficulty=0, buff=None) -> None:
        self.texture = texture
        self.description = description
        self.traversable_difficulty = traversable_difficulty
        self.buff = buff