from Goal import Goal
from abc import ABC, abstractmethod


class PrioritizedGoal(Goal):
    def __init__(self, priority: int, goal: Goal) -> None:
        super().__init__()
        self.priority = priority
        self.goal = goal
        self.running = False

    def start_executnig(self):
        if not self.is_running():
            self.running = True
            super().start_executnig()

    def should_continue_executing(self):
        return super().should_continue_executing()
    
    def tick(self):
        return super().tick()

    def is_preemtible(self):
        return super().is_preemtible()

    def is_preemtible_by(self, other: "PrioritizedGoal"):
        return self.is_preemtible() and other.get_priority() < self.get_priority()
    
    def get_priority(self):
        return self.priority 
    
    def get_goal(self):
        return self.goal
    
    def is_running(self):
        return self.running
    
    def __str__(self) -> str:
        return super().__str__

    def __hash__(self) -> int:
        return super().__hash__()
    
    def __eq__(self, __value: object) -> bool:
        if self is __value:
            return True
        else:
            return __value != None and self.__class__ == __value.__class__ and self.goal == __value.goal