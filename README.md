# What is this project?

This Django project serves as a RESTful API for managing movie-related data. It provides endpoints to interact with movie information.

## Installation

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

To interact with the MovieAPI:

1. **Retrieve all movies**: Send a GET request to `/movies/`.
2. **Retrieve details of a movie**: Send a GET request to `/movies/{movie_id}/`.

For genre-specific movies:

1. **Action movies**: Access `/action/` to get a list of action movies.
2. **Comedy movies**: Access `/comedy/` to get a list of comedy movies.

