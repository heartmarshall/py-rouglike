from abc import ABC, abstractmethod
from enum import Enum

class Goal(ABC):

    def __init__(self) -> None:
        pass

    def should_execute(self):
        pass

    def should_continue_executing(self):
        return self.should_execute()
    
    def is_preemtible(self):
        return True
    
    def start_executnig(self):
        pass

    def reset_task(self):
        pass

    def tick(self):
        pass
    
    def __str__(self) -> str:
        return str(self.__class__)