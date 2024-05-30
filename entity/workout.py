class Workout:
    def __init__(
        self, workout_id, user_id, workout_type, duration, intensity, log_date
    ):
        self.workout_id = workout_id
        self.user_id = user_id
        self.workout_type = workout_type
        self.duration = duration
        self.intensity = intensity
        self.log_date = log_date
