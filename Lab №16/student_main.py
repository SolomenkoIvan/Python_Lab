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

# Example usage
schedule = Schedule()

task1 = Task(title="Buy groceries", description="Milk, Bread, Eggs", due_date=date(2024, 6, 5))
schedule.add_task(task1)
print(schedule.list_all_tasks())

print(schedule.list_overdue_tasks())

task2 = Task(title="Submit assignment", description="Math assignment", due_date=date(2024, 6, 8))
schedule.add_task(task2)
print(schedule.list_all_tasks())

schedule.mark_as_completed("Buy groceries")
print(schedule.get_task("Buy groceries").status)

schedule.update_task("Buy groceries", description="Milk, Bread, Eggs, Cheese", due_date=date(2024, 5, 26))
print(schedule.get_task("Buy groceries"))

print(schedule.list_overdue_tasks())

print(schedule.list_tasks_due_today())

task3 = Task(title="Water plants", description="Water the plants in the garden", due_date=date(2024, 5, 25), duration=2)
schedule.add_task(task3)
print(schedule.list_tasks_by_duration(1, 3))

print(schedule.list_all_tasks())
