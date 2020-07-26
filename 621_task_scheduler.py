from collections import Counter
from typing import List

class Task:
    def __init__(self, name, count, cool = 0):
        self.name = name
        self.count = count
        self.cool = cool
        
    def reduce_cool(self):
        if self.cool > 0:
            self.cool -= 1
    
    def is_cool_zero(self):
        return self.cool == 0
    
    def add_cool(self, n):
        if self.cool == 0:
            self.cool = n
        else:
            raise ValueError("Task is still cooling")
        
class AllTasks:
    def __init__(self, task_counts: Counter, n: int):
        self.all_tasks = []
        self.total_tasks = 0
        self.n = n
        for task_name in task_counts:
            self.total_tasks += task_counts[task_name]
            t = Task(task_name, task_counts[task_name])
            self.all_tasks.append(t)

        #print(self.all_tasks)
        #print(self.total_tasks)
            
    def get_most_frequent_task_with_zero_cool(self) -> Task:
        self.all_tasks.sort(key=lambda t: t.count, reverse=True)
        for task in self.all_tasks:
            if task.cool == 0 and task.count > 0:
                return task
        return None
    
    def are_tasks_complete(self):
        return self.total_tasks == 0
    
    def update_cool_all_tasks(self, current_task: Task):
        if current_task:
            for task in self.all_tasks:
                if task.name == current_task.name:
                    task.count -= 1
                    self.total_tasks -= 1
                    task.add_cool(self.n)
                else:
                    task.reduce_cool()
        else:
            for task in self.all_tasks:
                task.reduce_cool()
            
        
        
        
class Solution:
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        all_tasks = AllTasks(task_counts, n)
        cycles = 0
        while not all_tasks.are_tasks_complete():
            cycles += 1
            task = all_tasks.get_most_frequent_task_with_zero_cool()
            all_tasks.update_cool_all_tasks(task)
            
        return cycles


#s = Solution()
# print(s.leastInterval(["A","A","A","B","B","B"], 2))
#print(s.leastInterval(["A","A","A","B","B","B"], 0))