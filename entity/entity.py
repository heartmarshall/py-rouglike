from world.cell import Cell


class Entity:
    def __init__(self, position: Cell) -> None:
        self.x = position.x
        self.y = position.y
    
    def set_position(self, position: Cell):
        self.x = position.x
        self.y = position.y
    
    def get_distance(self, other_entity: 'Entity'):
        dx = self.x - other_entity.x;
        dy = self.x - other_entity.x;
        return (dx**2 + dy**2)**(0.5)

    def can_be_pushed(self):
        return False

    def can_be_collided(self):
        return False