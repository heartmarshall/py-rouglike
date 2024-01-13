from abc import ABC, abstractmethod
from world import World
from mob_entity import MobEntity

class PathNavigator(ABC):
    def __init__(self, entity: MobEntity, world: World) -> None:
        self.entity = entity
        self.world = world

    @abstractmethod
    def getTargetPos(self):
      return self.target_pos
    
