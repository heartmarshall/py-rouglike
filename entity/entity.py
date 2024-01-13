from world.cell import Cell
from world.team import Team


class Entity:
    def __init__(self, position: Cell, team=Team.Enemy) -> None:
        self.x = position.x
        self.y = position.y
        self.team = team
    
    def set_position(self, position: Cell):
        self.x = position.x
        self.y = position.y
    
    def get_distance(self, other_entity: 'Entity'):
        dx = self.x - other_entity.x;
        dy = self.x - other_entity.x;
        return (dx**2 + dy**2)**(0.5)

    def is_entity_in_range(self, entity: 'Entity', distance: float):
        dx = self.x - entity.x
        dy = self.y - entity.y
        return (dx**2 + dy **2) < distance**2
    
    def tick(self):
        self.base_tick()

    def base_tick(self):
        pass

    def __hash__(self) -> int:
        return str((self.x, self.y, str(self.__class__)))

    @property
    def move_events_triger():
        return True