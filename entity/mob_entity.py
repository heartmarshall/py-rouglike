from entity.entity import Entity
from world.cell import Cell
from inventory import Inventory


class MobEntity(Entity):
    def __init__(self, position: Cell, ) -> None:
        super().__init__(position)
    
