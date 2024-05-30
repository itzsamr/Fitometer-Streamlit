CREATE DATABASE FitometerDB;

USE FitometerDB;

CREATE TABLE users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(256) NOT NULL
);

CREATE TABLE workouts (
    workout_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT FOREIGN KEY REFERENCES users(user_id),
    workout_type NVARCHAR(50),
    duration INT,
    intensity NVARCHAR(50),
    log_date DATETIME DEFAULT GETDATE()
);

