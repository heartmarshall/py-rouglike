from collections import deque


class GameSheduler:
    def __init__(self) -> None:
        self.queue = deque()
        self.all_entities = set()
    
    def add_entity(self, entity):
        self.queue.append(entity)
    
    def get_next(self):
        if self.queue:
            next_entity = self.queue.popleft()
            if next_entity not in self.all_entities:
                return self.get_next()
            self.queue.append(next_entity)
            return next_entity
        return False
    
    def remove_entity(self, enity):
        self.all_entities.remove(enity)

    