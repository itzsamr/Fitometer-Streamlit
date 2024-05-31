import pandas as pd
import hashlib
from util.DBConnection import DBConnection


class Implementation:
    def __init__(self):
        self.conn_util = DBConnection()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate_user(self, username, password):
        conn = self.conn_util.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT user_id, password FROM users WHERE username=?", (username,)
        )
        result = cursor.fetchone()
        conn.close()
        if result and self.hash_password(password) == result[1]:
            return result[0]
        return None

    def register_user(self, username, password):
        conn = self.conn_util.get_db_connection()
        cursor = conn.cursor()
        hashed_password = self.hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password),
        )
        conn.commit()
        conn.close()

    def get_user_id(self, username):
        conn = self.conn_util.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None

    def log_workout(self, user_id, workout_type, duration, intensity):
        conn = self.conn_util.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO workouts (user_id, workout_type, duration, intensity) VALUES (?, ?, ?, ?)",
            (user_id, workout_type, duration, intensity),
        )
        conn.commit()
        conn.close()

    def fetch_workouts(self, user_id):
        conn = self.conn_util.get_db_connection()
        query = "SELECT workout_type, duration, intensity, log_date FROM workouts WHERE user_id=?"
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
        conn.close()
        workouts = []
        for row in rows:
            workout = {
                "workout_type": row[0],
                "duration": row[1],
                "intensity": row[2],
                "log_date": row[3],
            }
            workouts.append(workout)
        return workouts
