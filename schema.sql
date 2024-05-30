CREATE DATABASE FitometerDB;

USE FitometerDB;

CREATE TABLE users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(256) NOT NULL
);

CREATE TABLE exercises (
    exercise_id INT PRIMARY KEY IDENTITY(1,1),
    exercise_name NVARCHAR(100) NOT NULL,
    description NVARCHAR(MAX)
);

CREATE TABLE workouts (
    workout_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT FOREIGN KEY REFERENCES users(user_id),
    workout_type NVARCHAR(50),
    duration INT,
    intensity NVARCHAR(50),
    log_date DATETIME DEFAULT GETDATE()
);

CREATE TABLE workout_exercises (
    workout_id INT,
    exercise_id INT,
    sets INT,
    reps INT,
    rest_interval INT,
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id),
    PRIMARY KEY (workout_id, exercise_id)
);

CREATE TABLE progress_tracking (
    progress_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT FOREIGN KEY REFERENCES users(user_id),
    workout_id INT FOREIGN KEY REFERENCES workouts(workout_id),
    workout_date DATE,
    calories_burned INT,
    duration INT,
    sets_completed INT,
    reps_completed INT
);
