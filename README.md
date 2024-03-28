# Django URL Archiver API

## Introduction

Welcome to the Django URL Archiver API repository. This API is built using the Django Rest Framework and is designed to archive URLs by creating a hash of their content using the SHA256 algorithm. By hashing the content of web pages, we ensure that the integrity of the saved snapshots is preserved and contents are not altered over time.

## Features

- **URL Archiving**: Archive a given URL by hashing its content with the SHA256 algorithm.
- **Content Verification**: Check the archived snapshot against the current webpage to ensure it is up-to-date.
- **Archived Pages List**: Receive a list of all archived pages including their metadata.
- **Page Snapshots List**: Retrieve a list of snapshots for a given URL, enabling users to see the history of that page's content.

## How to Use

This API provides the following endpoints:

1. **Hash URL**
   - `POST /hashurl`
   - This endpoint receives a URL and archives its content by creating a hash with the SHA256 algorithm.

2. **Check Snapshot**
   - `GET /check?snapshot_id=<UUID>`
   - This endpoint allows you to check an archived snapshot against the current version of the page to verify if it's still up-to-date.

3. **List Archived Pages**
   - `GET /list`
   - This endpoint provides a list of all archived pages, including their URL, the date of archiving, and the hash value.

4. **List Page Snapshots**
   - `GET /listpages?url=<URL>`
   - This endpoint retrieves all snapshots made for the given URL.

## Installation

To install this API on your local system, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/username/django-url-archiver-api.git
   ```

2. Navigate to the cloned repository:
   ```
   cd django-url-archiver-api
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```
   python manage.py migrate
   ```

5. Start the server:
   ```
   python manage.py runserver
   ```

Your API should now be running and accessible at `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions from the community. Please feel free to fork the repository, make your changes and submit a pull request. If you discover issues or have suggestions for improvements, please open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Thank you for using or contributing to the Django URL Archiver API!
