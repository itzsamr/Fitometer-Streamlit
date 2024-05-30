from abc import ABC, abstractmethod


class ServiceProvider(ABC):
    @abstractmethod
    def authenticate_user(self, username, password):
        pass

    @abstractmethod
    def register_user(self, username, password):
        pass

    @abstractmethod
    def log_workout(self, user_id, workout_type, duration, intensity):
        pass

    @abstractmethod
    def fetch_workouts(self, user_id):
        pass
