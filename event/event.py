from enum import Enum

class EventTrigger(Enum):
    KILL = "KillEvent"
    STEP_ON_CELL = "StepOnCellEvent"
    DEATH = "DeathEvent"
    MOVE = "MoveEvent"
    TURN_COUNT = "TurnCountEvent"

class Event:
    def __init__(self, event_trigger, world):
        self.event_trigger = event_trigger
        self.world = world

    def activate(self):
        pass

class KillEvent(Event):
    def __init__(self, killer_entity, victim_entity, world):
        super().__init__(EventTrigger.DEATH, world)
        self.killer_entity = killer_entity
        self.victim_entity = victim_entity

    def activate(self):
        print(f"{self.dying_entity} died")

class StepOnCellEvent(Event):
    def __init__(self, cell, world):
        super().__init__(EventTrigger.STEP_ON_CELL, world)
        self.cell = cell

    def activate(self, steped_entity):
        print(f"{steped_entity} steped on {self.cell}.")

class MoveEvent(Event):
    def __init__(self, enity, direction, world):
        super().__init__(EventTrigger.MOVE, world)
        self.entity = enity
        self.direction = direction

    def activate(self):
        print(f"{self.entity} moved {self.direction}.")

class DeathEvent(Event):
    def __init__(self, entity, world):
        super().__init__(EventTrigger.DEATH, world)
        self.dying_entity = entity

    def activate(self):
        print(f"{self.dying_entity} died.")

class TurnCountEvent(Event):
    def __init__(self, turn_count, world):
        super().__init__(EventTrigger.TURN_COUNT, world)
        self.turn_count = turn_count

    def activate(self):
        print(f"Reached {self.turn_count} turns.")

class DropItemsEvent(DeathEvent):
    def __init__(self, entity: MobEntity, world:World):
        super().__init__(entity, world)
        self.entity_cell = self.world.map.cell_info(entity.x, entity.y)

    def activate(self):
        self.entity_cell.inventory.extend(self.entity.inventory)


    