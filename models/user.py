from .habit import Habit

class User:
    def __init__(self, name: str):
        self.name = name
        self.habits = []

    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    def get_habit(self, habit_name: str):
        for habit in self.habits:
            if habit.name == habit_name:
                return habit
        return None
