from world.cell import Cell
from world.team import Team


class Entity:
    def __init__(self, position: Cell, sprite, team=Team.Monster) -> None:
        self.x = position.x
        self.y = position.y
        self.sprite = sprite
        self.team = team

    def setPosition(self, position: Cell):
        self.x = position.x
        self.y = position.y
    
    def getDistance(self, other_entity: 'Entity'):
        dx = self.x - other_entity.x
        dy = self.x - other_entity.x
        return (dx**2 + dy**2)**(0.5)

    def isEntityInRange(self, entity: 'Entity', distance: float):
        dx = self.x - entity.x
        dy = self.y - entity.y
        return (dx**2 + dy **2) < distance**2
    
    def tick(self):
        self.base_tick()

    def base_tick(self):
        pass

    def __hash__(self) -> int:
        return str((self.x, self.y, str(self.__class__)))