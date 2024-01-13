from entity.entity import Entity
from world.cell import Cell
from item.inventory import Inventory
from input_listener import InputListener
from stats import Stats

class PlayerEntity(Entity):
    def __init__(self, position: Cell) -> None:
        super().__init__(position)
        self.inventory = Inventory()
        self.input_listener = InputListener()
        self.stats = Stats(100, 100, 10, 10, 2)
            
    def is_dead(self):
        return self.stats.hp <= 0
    
    