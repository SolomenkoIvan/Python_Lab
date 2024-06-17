Лабораторна робота №16: Advanced TODO list 

Мета роботи: Створити систему управління завданнями та розкладом використовуючи Python система складається з класів Task та Schedule надає можливість додавати оновлювати сортувати завдання та керувати різними атрибутами такими як терміни виконання пріоритет статус нотатки та залежності також система підтримує операції з файлами для збереження та завантаження розкладів і надає нагадування та повідомлення про майбутні завдання кінець проекту користувач зможе ефективно керувати своїми завданнями та розкладом використовуючи реалізовані класи та методи це допоможе користувачам бути організованими дотримуватися термінів та підвищувати продуктивність


Опис завдання: 
``` 
Task 1: Create Task Class
Create a Python class named Task with the following attributes:
title
description
due_date (use datetime.date )
Example of class usage:
Task 2: Add Method to Task Class
Add a method named is_due_today() to the Task class that checks if the task is due today and returns a boolean.
Example of class usage:
 
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
task.is_due_today()  # Expected output: True if today is the due
date
Task 3: Create Schedule Class
Create a class named Schedule that manages multiple tasks. It should have the following methods:
add_task(task: Task)
      remove_task(task_title: str)
     get_task(task_title: str) -> Task
Example of class usage:
  schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.get_task("Buy groceries")  # Expected output: Task
object
Task 4: List Overdue Tasks
Add a method named list_overdue_tasks() to the Schedule class that returns a list of tasks that are overdue.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() - timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=2))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_overdue_tasks()  # Expected output: [task1]
Task 5: List Tasks Due Today
Add a method named list_tasks_due_today() to the Schedule class that returns a list of tasks that are due today.
Example of class usage:
   from datetime import date
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())

 task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today())
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_due_today()  # Expected output: [task1,
task2]
Task 6: Sort Tasks by Due Date
Add a method named sort_tasks_by_due_date() to the Schedule class that returns a list of tasks sorted by their due dates.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() + timedelta(days=2))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.sort_tasks_by_due_date()  # Expected output: [task2,
task1]
Task 7: Update Task
Add a method named update_task(task_title: str, **kwargs) to the Schedule class that updates the attributes of a task.
Example of class usage:
   schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.update_task("Buy groceries", description="Milk, Bread,
Eggs, Cheese", due_date=date(2024, 5, 26))
schedule.get_task("Buy groceries")  # Expected output: Task
object with updated attributes

Task 8: Task Status
Add a status attribute to the class which can be 'Pending', 'In Progress', or
  'Completed'. Modify Task and Example of class usage:
to handle task status updates.
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Pending")
schedule = Schedule()
schedule.add_task(task)
task.status = "In Progress"
schedule.update_task("Buy groceries", status="Completed")
schedule.get_task("Buy groceries").status  # Expected output:
"Completed"
Task 9: Weekly Schedule
Create a method weekly_schedule(start_date: date) in the Schedule class that returns a list of tasks for the week starting from the provided date.
Example of class usage:
   from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 5, 23))
schedule.add_task(task1)
schedule.add_task(task2)
start_date = date(2024, 5, 20)
schedule.weekly_schedule(start_date)  # Expected output: [task1,
task2]
Task 10: Monthly Schedule
Create a method monthly_schedule(year: int, month: int) in the Schedule class that returns a list of tasks for the specified month.
  Example of class usage:
Task
 Schedule

 from datetime import date
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 6, 1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.monthly_schedule(2024, 5)  # Expected output: [task1]
Task 11: Task Priority
Add a priority attribute to the Task class which can be 'Low', 'Medium', or 'High'. Modify Task and Schedule to handle task priority.
Example of class usage:
Task 12: List Tasks by Priority
Add a method list_tasks_by_priority(priority: str) to the Schedule class that returns a list of tasks with the specified priority.
Example of class usage:
    task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
schedule = Schedule()
schedule.add_task(task)
task.priority  # Expected output: "High"
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), priority="Low")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_by_priority("High")  # Expected output:
[task1]

Task 13: Save Schedule to File
Add a method save_to_file(filename: str) to the Schedule class that saves the schedule to a file.
Example of class usage:
Task 14: Load Schedule from File
Add a method load_from_file(filename: str) to the Schedule class that loads the schedule from a file.
   schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.save_to_file("schedule.txt")
  Example of class usage:
Task 15: Task Notes
Add a notes attribute to the the task. Modify Task and
Example of class usage:
class that can store additional information about to handle task notes.
 schedule = Schedule()
schedule.load_from_file("schedule.txt")
 Task
  Schedule
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
schedule = Schedule()
schedule.add_task(task)
task.notes  # Expected output: "Use the discount coupon"
Task 16: List Tasks with Notes
Add a method list_tasks_with_notes() to the Schedule class that returns a list of tasks that have notes.
  
Example of class usage:
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_with_notes()  # Expected output: [task1]
Task 17: Mark Task as Completed
Add a method mark_as_completed(task_title: str) to the Schedule class that marks the specified task as completed.
Example of class usage:
   task = Task(title="Buy groceries", description="Milk, Bread, Eggs
", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.mark_as_completed("Buy groceries")
task.status  # Expected output: "Completed"
Task 18: List Completed Tasks
Add a method list_completed_tasks() to the Schedule class that returns a list of completed tasks.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)

 schedule.add_task(task2)
schedule.list_completed_tasks()  # Expected output: [task1]
Task 19: Find Task by Keyword
Add a method find_task_by_keyword(keyword: str) to the Schedule class that returns a list of tasks that contain the specified keyword in their title or description.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.find_task_by_keyword("assignment")  # Expected output:
[task2]
Task 20: Task Deadline Notification
Add a method check_deadlines() to the Schedule class that returns a list of tasks that are due in the next 24 hours.
Example of class usage:
   from datetime import datetime, timedelta
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=datetime.now().date() + timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=datetime.now().date() + timedelta(days=2))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.check_deadlines()  # Expected output: [task1]
Task 21: List All Tasks

  Add a method list_all_tasks() to the Schedule class that returns a list of all tasks.
Example of class usage:
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_all_tasks()  # Expected output: [task1, task2]
Task 22: Task Duration
Add a duration attribute to the class which specifies the expected time to complete the task in hours. Modify and Schedule to handle task duration.
Example of class usage:
Task 23: List Tasks by Duration
Add a method
int) to the class that returns a list of tasks whose duration falls within
the specified range.
Example of class usage:
 Task
  Task
 task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
schedule = Schedule()
schedule.add_task(task)
task.duration  # Expected output: 2
 list_tasks_by_duration(min_duration: int, max_duration:
  Schedule
 task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), duration=4)
schedule = Schedule()
schedule.add_task(task1)

 schedule.add_task(task2)
schedule.list_tasks_by_duration(1, 3)  # Expected output: [task1]
Task 24: Task History
Add a method task_history() to the Schedule class that returns a history of tasks added, removed, and updated in the schedule.
Example of class usage:
   schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task1)
schedule.remove_task("Buy groceries")
schedule.task_history()  # Expected output: [("added", task1),
("removed", task1)]
Task 25: Clear Completed Tasks
Add a method clear_completed_tasks() to the Schedule class that removes all completed tasks from the schedule.
Example of class usage:
   task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.clear_completed_tasks()
schedule.list_all_tasks()  # Expected output: [task2]
Task 26: Task Recurrence
Add a recurrence attribute to the   class that specifies if the task is recurring (daily, weekly, monthly). Modify   and Schedule to handle task recurrence.
Task
 Example of class usage:
Task

 task = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
schedule = Schedule()
schedule.add_task(task)
task.recurrence  # Expected output: "weekly"
Task 27: List Recurring Tasks
Add a method list_recurring_tasks() to the Schedule class that returns a list of recurring tasks.
Example of class usage:
   task1 = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_recurring_tasks()  # Expected output: [task1]
Task 28: Task Reminders
Add a method set_reminder(task_title: str, reminder_date: date) to the Schedule class that sets a reminder for a specific task.
Example of class usage:
   task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.set_reminder("Buy groceries", date(2024, 5, 24))
 Task 29: Task Completion Percentage
Add a method completion_percentage() to the Schedule class that returns the percentage of completed tasks.
  
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.completion_percentage()  # Expected output: 50.0
Task 30: Task Dependency
Add a dependencies attribute to the Task class that specifies other tasks that need to be completed before the task can start. Modify Task and Schedule to handle task dependencies.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Prepare breakfast", description="Use
groceries to prepare breakfast", due_date=date(2024, 5, 26),
dependencies=[task1])
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
task2.dependencies  # Expected output: [task1]
___
Виконання роботи: 
Python
from datetime import date, datetime, timedelta

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes="", duration=0, recurrence=None, dependencies=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies if dependencies else []

    def is_due_today(self):
        return self.due_date == date.today()

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, due_date={self.due_date}, status={self.status}, priority={self.priority}, notes={self.notes}, duration={self.duration}, recurrence={self.recurrence}, dependencies={[dep.title for dep in self.dependencies]})"

class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(("added", task))

    def remove_task(self, task_title):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(("removed", task))

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.due_date < date.today() and task.status != "Completed"]

    def list_tasks_due_today(self):
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self):
        return sorted(self.tasks, key=lambda task: task.due_date)

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self.history.append(("updated", task))

    def weekly_schedule(self, start_date):
        end_date = start_date + timedelta(days=7)
        return [task for task in self.tasks if start_date <= task.due_date < end_date]

    def monthly_schedule(self, year, month):
        return [task for task in self.tasks if task.due_date.year == year and task.due_date.month == month]

    def list_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(repr(task) + '\n')

    def load_from_file(self, filename):
        self.tasks.clear()
        with open(filename, 'r') as file:
            for line in file:
                task_repr = line.strip()
                task = eval(task_repr)
                self.add_task(task)

    def list_tasks_with_notes(self):
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
            self.history.append(("updated", task))

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    def check_deadlines(self):
        next_24_hours = date.today() + timedelta(days=1)
        return [task for task in self.tasks if task.due_date == next_24_hours]

    def list_all_tasks(self):
        return self.tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self):
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self):
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.status == "Completed"])
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    def __repr__(self):
        return f"Schedule(tasks={self.tasks}, history={self.history})"
___
Результати:
Python
[Task(title=Buy groceries, description=Milk, Bread, Eggs, due_date=2024-06-05, status=Pending, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[])]
[Task(title=Buy groceries, description=Milk, Bread, Eggs, due_date=2024-06-05, status=Pending, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[])]
[Task(title=Buy groceries, description=Milk, Bread, Eggs, due_date=2024-06-05, status=Pending, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[]), Task(title=Submit assignment, description=Math assignment, due_date=2024-06-08, status=Pending, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[])]
Completed
Task(title=Buy groceries, description=Milk, Bread, Eggs, Cheese, due_date=2024-05-26, status=Completed, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[])
[Task(title=Submit assignment, description=Math assignment, due_date=2024-06-08, status=Pending, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[])]
[]
[Task(title=Water plants, description=Water the plants in the garden, due_date=2024-05-25, status=Pending, priority=Medium, notes=, duration=2, recurrence=None, dependencies=[])]
[Task(title=Buy groceries, description=Milk, Bread, Eggs, Cheese, due_date=2024-05-26, status=Completed, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[]), Task(title=Submit assignment, description=Math assignment, due_date=2024-06-08, status=Pending, priority=Medium, notes=, duration=0, recurrence=None, dependencies=[]), Task(title=Water plants, description=Water the plants in the garden, due_date=2024-05-25, status=Pending, priority=Medium, notes=, duration=2, recurrence=None, dependencies=[])]

```

Висновки: Цей код реалізує систему управління завданнями з двома основними класами: Task для опису завдань і Schedule для їх керування. Система дозволяє додавати, видаляти, оновлювати завдання, сортувати їх за різними критеріями, відстежувати виконання, зберігати та завантажувати завдання з файлу, а також керувати історією змін. Це забезпечує зручне та ефективне управління завданнями.