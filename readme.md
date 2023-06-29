Sure, here's an updated README with a section on setting up the application's configuration:

---

# GitHub OAuth Flask Application

This is a Flask application that allows users to log in using GitHub OAuth and perform CRUD operations on their personal profile.

## Features

- GitHub OAuth for user authentication
- CRUD operations for user profile
- SQLAlchemy for database operations

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Docker

### Configuration

This application uses environment variables for configuration. You can set these variables in a `.env` file in the root directory of the project. Here's an example `.env` file:

```bash
LOG_LEVEL=DEBUG
APP_HOST=localhost
APP_PORT=5000
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
GITHUB_REDIRECT_URI=http://localhost:5000/github/callback
API_SECRET_KEY=your_secret_key
DB_URI=your_database_uri
OAUTHLIB_INSECURE_TRANSPORT=1
```

Replace `your_github_client_id`, `your_github_client_secret` these variables are mandatory.

Add your private `your_secret_key` or it's gonna be generated with UUID

Add you database `your_database_uri` with your actual values, default value configured for the docker-compose postgresql: . 

Tested with postgresql and sqlite3

### Installation

1. Clone the repository:

```bash
git clone https://github.com/botondberde/Wolf_Badger_techincal_test.git
```

2. Navigate to the project directory:

```bash
cd Wolf_Badger_techincal_test
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```
4.Run database compose-file or use your own
```bash
docker-compose -f build/docker-compose.yml up -d
```

5. Run the application:

```bash
python main.py
```


The application will be available at `http://localhost:5000`.

## Usage

Once you've started the application, navigate to `http://localhost:5000` in your web 
browser. From there, you can log in with GitHub
After that you're able to use create, read, update, and delete your user profile with the following endpoints:


## Endpoint Description
The Flask application exposes the following endpoints:

GET /login

Description: Initiates the GitHub account login process using Flask Dance and initializes the database.
Response: A message indicating the GitHub username of the logged-in user.


POST /user

Description: Creates a new user if the user is authenticated.
Request Body: JSON object representing the user details.
Response: The ID of the created user.


GET /user/{id}

Description: Retrieves a user by their ID.
Path Parameter: id - ID of the user to retrieve.
Response: JSON object containing the user details.

GET /users

Description: Retrieves all user.
Response: JSON array containing all user details.


PUT /user/{id}

Description: Updates a user by their ID.
Path Parameter: id - ID of the user to update.
Request Body: JSON object representing the user details to be updated.
Response: JSON object containing the updated user details.


DELETE /user/{id}

Description: Deletes a user by their ID.
Path Parameter: id - ID of the user to delete.
Response: Empty response with a success status.

## User object:
```python

id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(80), nullable=False) #Mandatory for user creation
email = db.Column(db.String(120), unique=True) #Mandatory for user creation
location = db.Column(db.String(120))
```
---

## Local testing

# Run unit tests
```bash
python -m modules.api.tests_app
```
# Run talend API tests

Download and install talend API tester plugin
import the file `wolf_badger_talend_api.json` in the plugin

Navigate to `http://localhost:5000` in your web browser. From there, you can log in with GitHub

After the login you're able to execute the requests

