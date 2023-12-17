from Goal import Goal
from PrioritizedGoal import PrioritizedGoal
import heapq


class DUMMY_GOAL(Goal):
            def should_execute(self):
                return False
            def is_running(self):
                return False
            
class GoalSelector:
    def __init__(self) -> None:        
        self.DUMMY = PrioritizedGoal(9999, DUMMY_GOAL())
        self.goals = set()
        self.running_goal = self.DUMMY

    def add_goal(self, priority: int, task: Goal):
        self.goals.add(PrioritizedGoal(priority, task))
    
    def remove_goal(self, task: Goal):
        # Делаем reset всех задач, которые сейчас будем отменять
        for goal in self.goals:
             if goal.get_goal() == task and goal.is_running():
                  goal.reset_task()
        # Удаляем их из goals
        self.goals.difference_update({goal for goal in self.goals if goal.get_goal() == task})

    # Я отказался от идеи нескольких одновременно выполняемых задач
    # def get_running_goals(self):
    #      return {goal for goal in self.goals if goal.is_running()}
    
    def tick(self):
        # running goal Cleanup
        if not self.running_goal.is_running() or not self.running_goal.should_continue_executing():
            goal.reset_task()
        
        # goals Update
        for goal in self.goals:
            if not goal.is_running() and self.running_goal.is_preemtible_by(goal) and goal.should_execute():
                self.running_goal = goal
        
        # Запускаем выполнение выбранной цели (Если она сменилась)
        if not self.running_goal.is_running():
            self.running_goal.start_executnig()
        
        # goal Tick
        self.running_goal.tick()
