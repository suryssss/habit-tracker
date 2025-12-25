from datetime import date
from models.habit import Habit

class HabitManager:
    def __init__(self, user):
        self.user = user

    def create_habit(self, name: str, frequency="daily"):
        habit = Habit(name, frequency)
        self.user.add_habit(habit)

    def complete_habit(self, habit_name: str, log_date):
        habit = self.user.get_habit(habit_name)
        if not habit:
            raise ValueError("Habit not found")

        habit.mark_completed(log_date)

    def get_habit_names(self):
        return [habit.name for habit in self.user.habits]


    def complete_habit_today(self, habit_name: str):
        self.complete_habit(habit_name, date.today())

    def list_habits(self):
        return [
            (habit.name, habit.current_streak, habit.longest_streak)
            for habit in self.user.habits
        ]
