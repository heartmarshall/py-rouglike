from terrain.terrain import Terrain
from point import Point
from entity.entity import Entity
from event.event import EventTrigger
from collections import defaultdict

class Cell(Point):
    def __init__(self, x:int, y:int, terrain_type, items=None, occupied_by=None):
        super().__init__(x, y)
        self.terrain_type = terrain_type
        self.items = items or []
        self.occupied_by = occupied_by
        self.events = defaultdict(set)

    def getTraversableDifficulty(self):
        return self.terrain_type.traversable_difficulty
    
    def isOcupied(self):
        return self.occupied_by is not None
    
    def removeOcupantEntity(self):
        self.occupied_by = None
    
    def tryToPlaceEntity(self, entity: Entity, move_event_triger=True) -> bool:
        """
        Попытка разместить сущность в ячейке карты.

        Params:
        - entity (Entity): Сущность, которую пытаемся разместить в ячейке.
        - move_event_trigger (bool, optional): Флаг, указывающий, следует ли активировать события при перемещении
        по клетке (по умолчанию True).

        Return:
        - bool: True, если размещение сущности в ячейке успешно; False, если ячейка уже занята.
        """
        if self.isOcupied():
            return False
        if move_event_triger and self.events[EventTrigger.STEP_ON_CELL]:
            for event in self.events[EventTrigger.STEP_ON_CELL]:
                event.activate(entity)
        self.occupied_by = entity
        return True

    