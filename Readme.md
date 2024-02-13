# Task Manager API

## Overview

Task Manager API is a Django REST framework application that provides endpoints for managing tasks.
It supports basic CRUD operations for individual tasks, as well as bulk creation and deletion of tasks.

## Postman Collection

For easy testing and interaction with the Task Manager API, you can use the provided Postman collection. 
This collection includes pre-configured requests for various API endpoints.

[Postman Collection](https://www.postman.com/anikettiwarime/workspace/water-dip-ai-backend-assignment/collection/22930511-0f26c3a0-2345-422a-8979-1634aec465c0?action=share&creator=22930511)

Please follow the link above to import the collection into your Postman workspace and start testing the Task Manager API.

## Features

- Create, retrieve, update, and delete individual tasks
- List all tasks
- Bulk create tasks
- Bulk delete tasks

## Getting Started

### Prerequisites

- Python 3.10
- Django 5.0.2
- Django REST framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anikettiwarime/waterDipAiBackend-Task
    ```

2. Change into the project directory:

    ```bash
    cd waterDipAiBackend-Task
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API should now be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

- **List/Create Tasks**

    `GET /v1/tasks/` - Get a list of all tasks or create a new task.

- **Retrieve/Update/Delete Task**

    `GET /v1/tasks/<id>/` - Retrieve details of a specific task.

    `PUT /v1/tasks/<id>/` - Update details of a specific task.

    `DELETE /v1/tasks/<id>/` - Delete a specific task.

- **Bulk Create Tasks**

    `POST /v1/tasks/bulk-create/` - Bulk create tasks.

- **Bulk Delete Tasks**

    `DELETE /v1/tasks/bulk-delete/` - Bulk delete tasks.

## Testing

To run the tests, execute the following command:

```bash
python manage.py test
```

