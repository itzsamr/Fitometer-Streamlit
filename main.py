import streamlit as st
from dao.implementation import Implementation
from exception.custom_exceptions import AuthenticationError
import matplotlib.pyplot as plt


def main():
    st.title("Fitness Tracking Application")

    menu = ["Login", "Register", "Log Workout", "View Workouts", "Stats"]
    choice = st.sidebar.selectbox("Menu", menu)

    implementation = Implementation()

    if choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            try:
                user_id = implementation.authenticate_user(username, password)
                if user_id:
                    st.success(f"Logged in as {username}")
                    st.session_state["user_id"] = user_id
                else:
                    raise AuthenticationError
            except AuthenticationError:
                st.warning("Incorrect Username/Password")

    elif choice == "Register":
        st.subheader("Register Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            implementation.register_user(username, password)
            st.success("User registered successfully")

    elif choice == "Log Workout":
        user_id = st.session_state.get("user_id")
        if not user_id:
            st.warning("Please login first")
        else:
            st.subheader("Log Workout")
            workout_type = st.selectbox(
                "Workout Type", ["Cardio", "Strength", "Flexibility", "Balance"]
            )
            duration = st.number_input("Duration (minutes)", min_value=1)
            intensity = st.selectbox("Intensity", ["Low", "Medium", "High"])
            if st.button("Log Workout"):
                implementation.log_workout(user_id, workout_type, duration, intensity)
                st.success("Workout logged successfully")

    elif choice == "View Workouts":
        user_id = st.session_state.get("user_id")
        if not user_id:
            st.warning("Please login first")
        else:
            st.subheader("View Workouts")
            df = implementation.fetch_workouts(user_id)
            if not df.empty:
                st.table(df)
            else:
                st.write("No workouts logged yet")

    elif choice == "Stats":
        user_id = st.session_state.get("user_id")
        if not user_id:
            st.warning("Please login first")
        else:
            st.subheader("Workout Statistics")
            df = implementation.fetch_workouts(user_id)
            if not df.empty:
                st.write("Total Workouts:", len(df))
                st.write("Average Workout Duration:", df["duration"].mean())
                intensity_counts = df["intensity"].value_counts()
                plt.bar(intensity_counts.index, intensity_counts.values)
                plt.xlabel("Intensity")
                plt.ylabel("Count")
                plt.title("Workout Intensity Distribution")
                st.pyplot(plt)

            else:
                st.write("No workouts logged yet")


if __name__ == "__main__":
    main()
