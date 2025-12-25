from datetime import date
from .habit_log import HabitLog
from .habit_type import DailyHabit, WeeklyHabit


class Habit:
    def __init__(self, name: str, frequency: str = "daily"):
        self.name = name
        self.frequency = frequency

        if frequency == "daily":
            self.habit_type = DailyHabit()
        elif frequency == "weekly":
            self.habit_type = WeeklyHabit()
        else:
            raise ValueError("Invalid habit frequency")

        self.logs = []
        self.current_streak = 0
        self.longest_streak = 0

    def mark_completed(self, log_date: date):
        for log in self.logs:
            if log.log_date == log_date:
                raise ValueError("Habit already marked for this date")

        self.logs.append(HabitLog(log_date, True))
        self._update_streak()

    def _update_streak(self):
        self.current_streak, self.longest_streak = \
            self.habit_type.calculate_streak(self.logs)

