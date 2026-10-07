# Login-Page
I am making loin page .
Author - Ravi Phaltakar.

# Python Login Page

A simple modern login page built with **Python and Tkinter**. This project is designed as a beginner-friendly Python project and can also be used to practice Git and GitHub.

## Features

- Modern dark-themed interface
- Username and password fields
- Password show/hide functionality
- Login validation
- Success and error messages
- Enter key support for login
- Separate files for UI, authentication, and styling
- Simple project structure suitable for GitHub practice

## Technologies Used

- Python 3
- Tkinter
- Git
- GitHub

## Project Structure

```text
login-page/
│
├── main.py
├── login.py
├── database.py
├── styles.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ravi-Phaltankar/Login-Page.git
```

### 2. Open the project

```bash
cd login-page
```

### 3. Run the application

```bash
python main.py
```

## Demo Credentials

You can use the following credentials:

| Username | Password |
|---|---|
| admin | 1234 |
| ravi | python123 |

## How It Works

The application is divided into multiple files:

### `main.py`

The entry point of the application.

It creates the `LoginApp` object and starts the application.

### `login.py`

Contains the main login interface and login functionality.

It handles:

- Creating the UI
- Reading username and password
- Password visibility
- Login validation
- Error and success messages

### `database.py`

Contains the demo user credentials and authentication function.

```python
authenticate_user(username, password)
```

### `styles.py`

Contains colors used throughout the application.

This keeps the styling separate from the application logic.

### `requirements.txt`

Contains information about project dependencies.

This project does not require external Python packages because Tkinter is included with standard Python installations.

## Security Note

This project is intended for learning purposes.

The demo version stores passwords as plain text. **Do not use this authentication approach in a production application.**

A production authentication system should use:

- Password hashing
- A proper database
- Secure session management
- Input validation
- Rate limiting
- HTTPS
- Secure password reset functionality

## Future Improvements

Possible improvements include:

- SQLite database
- Password hashing with bcrypt
- User registration
- Forgot password functionality
- Remember me option
- Login attempt limits
- User dashboard
- Form validation
- Database-backed authentication
- Application logging
- Unit tests

## Author

-Ravi Phaltankar

This project was created for learning Python, GUI development, and Git/GitHub workflows.
