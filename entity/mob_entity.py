from entity.entity import Entity
from world.cell import Cell

class MobEntity(Entity):
    def __init__(self, position: Cell) -> None:
        super().__init__(position)