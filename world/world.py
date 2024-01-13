from enum import Enum
from entity.entity import Entity
from map import Map
from sheduler.game_sheduler import GameSheduler
from entity.player_entity import PlayerEntity
from team import Team

class World:
    def __init__(self) -> None:
        self.entities = set()
        self.events = {}
        self.entities_counter = 0
        self.map = Map()
        self.sheduler = GameSheduler
        self.turn_counter = 0
        self.player_entity = None

    def spawn_entity(self, entity: Entity):
        cell = self.map.cellInfo(entity.x, entity.y)
        cell.try_to_place_entity(entity, move_event_triger=entity.move_events_triger)

    def move_entity(self, entity: Entity, new_x: int, new_y: int):
        old_cell = self.map.cellInfo(entity.x, entity.y)
        new_cell = self.map.cellInfo(new_x, new_y)
        if not new_cell.try_to_place_entity(entity, move_event_triger=entity.move_events_triger):
            return False
        old_cell.remove_ocupant_entity()
        return True

    def remove_entity(self, enity: Entity):
        cell = self.map.cellInfo(enity.x, enity.y)
        self.entities.remove(enity)
        cell.remove_ocupant_entity()

    def next_turn(self):
        self.turn_counter += 1
        entity = self.sheduler.get_next()
        if entity == self.player_entity:
            self.player_entity.make_turn()
        else:
            entity.tick()
    