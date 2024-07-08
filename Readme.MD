# Student Details CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using Python for backend logic, HTML for structure, CSS for styling, Bootstrap for UI components, Basic JavaScript for client-side interactions, and Docker for containerization.

## Functionality

- **Create:** Add new student details including first name, last name, email, and password.
- **Read (All):** Display a list of all student details.
- **Update:** Modify existing student details.
- **Delete:** Remove student records from the database.

## Technologies Used

- **Backend:** Python (Flask framework)
- **Frontend:** HTML, CSS, Bootstrap, Basic JavaScript
- **Database:** MySQL (or any other database supported by SQLAlchemy)
- **Containerization:** Docker

## Setup Instructions

### Prerequisites

- Python 3.8+
- Docker

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Build Docker image:
   ```bash
   docker build -t my-flask-app .
   ```

4. Run Docker container:
   ```bash
   docker run -p 8000:8000 my-flask-app
   ```

5. Access the application in your web browser:
   ```
   http://localhost:8000
   ```

## Directory Structure

```
.
├── app.py              # Main Flask application file
├── templates           # HTML templates
│   ├── index.html      # Homepage with student details listing
│   ├── add.html        # Form for adding new student details
│   └── update.html     # Form for updating student details
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration file
└── README.md           # This file
```

## Usage

- **Adding a New Student:** Click on "ADD STUDENT" button on the homepage and fill in the details.
- **Updating a Student:** Click on "UPDATE" button next to a student record on the homepage, make changes in the update form, and save.
- **Deleting a Student:** Click on "DELETE" button next to a student record on the homepage to delete the student record after confirmation.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
