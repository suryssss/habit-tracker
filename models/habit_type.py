from abc import ABC, abstractmethod

class HabitType(ABC):
    @abstractmethod
    def calculate_streak(self, logs):
        pass
class DailyHabit(HabitType):
    def calculate_streak(self, logs):
        if not logs:
            return 0, 0

        logs.sort(key=lambda x: x.log_date)

        streak = 1
        max_streak = 1

        for i in range(1, len(logs)):
            diff = (logs[i].log_date - logs[i - 1].log_date).days
            if diff == 1:
                streak += 1
            else:
                streak = 1
            max_streak = max(max_streak, streak)

        return streak, max_streak

class WeeklyHabit(HabitType):
    def calculate_streak(self, logs):
        if not logs:
            return 0, 0
        logs.sort(key=lambda x: x.log_date)
        streak = 1
        max_streak = 1
        for i in range(1, len(logs)):
            diff = (logs[i].log_date - logs[i - 1].log_date).days
            if 6 <= diff <= 8:
                streak += 1
            else:
                streak = 1

            max_streak = max(max_streak, streak)

        return streak, max_streak
