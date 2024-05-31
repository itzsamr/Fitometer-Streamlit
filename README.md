# Fitness Tracker - Fitometer

Fitometer is a fitness tracking web application built using Streamlit. It allows users to log their workouts, view workout history, and see statistics about their workouts.

## Features

- User authentication with hashlib (login and registration).
- Logging workouts with details such as workout type, duration, and intensity.
- Viewing workout history in a table format.
- Displaying statistics about logged workouts, including total workouts, average duration, and intensity distribution.
- Simple and intuitive user interface.

## Technologies Used

- Streamlit: For building the web application interface.
- Python: For backend logic and database management.
- SQLite: For storing user data and workout history.
- PyODBC: For connecting to the SQLite database.
- Matplotlib: For creating visualizations (workout intensity distribution).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/itzsamr/Fitometer-Streamlit.git
    cd Fitometer-Streamlit
    ```  
2. Run the application:
    ```bash
    streamlit run main.py
    ```

## Usage

1. Register or login with your username and password.
2. Log your workouts by selecting the "Log Workout" option and providing details.
3. View your workout history and statistics using the respective menu options.

## File Structure

- `main.py`: The main Streamlit application file.
- `dao/`: Directory containing data access object classes.
- `exception/`: Directory containing custom exception classes.
- `entity/`: Directory containing entity classes (Exercise, User, Workout).
- `util/`: Directory containing utility classes (DBConnection, PropertyUtil).

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.
