import streamlit as st
import pyodbc
import pandas as pd
import hashlib
import configparser


def get_db_connection():
    config = configparser.ConfigParser()
    config.read(
        "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/Fitometer/config.properties"
    )

    server_name = config.get("DATABASE", "server")
    database_name = config.get("DATABASE", "database")
    driver = config.get("DATABASE", "driver")

    conn_str = f"Driver={driver};Server={server_name};Database={database_name};Trusted_Connection=yes;"
    conn = pyodbc.connect(conn_str)
    return conn


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and hash_password(password) == result[1]:
        return result[0]
    return None


def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password),
    )
    conn.commit()
    conn.close()


def get_user_id(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None


def log_workout(user_id, workout_type, duration, intensity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO workouts (user_id, workout_type, duration, intensity) VALUES (?, ?, ?, ?)",
        (user_id, workout_type, duration, intensity),
    )
    conn.commit()
    conn.close()


def fetch_workouts(user_id):
    conn = get_db_connection()
    query = "SELECT workout_type, duration, intensity, log_date FROM workouts WHERE user_id=?"
    df = pd.read_sql(query, conn, params=(user_id,))
    conn.close()
    return df


def main():
    st.title("Fitness Tracking Application")

    menu = ["Login", "Register", "Log Workout", "View Workouts"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.success(f"Logged in as {username}")
                st.session_state["username"] = username
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "Register":
        st.subheader("Register Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            register_user(username, password)
            st.success("User registered successfully")

    elif choice == "Log Workout":
        if "username" not in st.session_state:
            st.warning("Please login first")
        else:
            st.subheader("Log Workout")
            workout_type = st.selectbox(
                "Workout Type", ["Cardio", "Strength", "Flexibility", "Balance"]
            )
            duration = st.number_input("Duration (minutes)", min_value=1)
            intensity = st.selectbox("Intensity", ["Low", "Medium", "High"])
            if st.button("Log Workout"):
                user_id = get_user_id(st.session_state["username"])
                log_workout(user_id, workout_type, duration, intensity)
                st.success("Workout logged successfully")

    elif choice == "View Workouts":
        if "username" not in st.session_state:
            st.warning("Please login first")
        else:
            st.subheader("View Workouts")
            user_id = get_user_id(st.session_state["username"])
            df = fetch_workouts(user_id)
            st.dataframe(df)


if __name__ == "__main__":
    main()
