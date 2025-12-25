from datetime import date

class HabitLog:
    def __init__(self, log_date: date, completed: bool):
        self.log_date = log_date
        self.completed = completed
