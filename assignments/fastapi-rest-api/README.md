# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework in Python. Students will create endpoints for managing items, use request validation, and explore FastAPI's automatically generated documentation.

## 📝 Tasks

### 🛠️ Create the API Structure

#### Description
Use FastAPI to define the application and build routes for listing and retrieving items.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Define a route at `/items/` that returns a list of item objects.
- Define a route at `/items/{item_id}` that returns a single item by its ID.
- Use Python dictionaries or a list to store example item data.

### 🛠️ Add Item Creation and Validation

#### Description
Add endpoints for creating new items and validating incoming request data.

#### Requirements
Completed program should:

- Define a POST route at `/items/` to add a new item.
- Use a Pydantic model to validate the request body.
- Return the created item with a success response.
- Include fields such as `name`, `description`, and `price`.

### 🛠️ Update and Delete Items

#### Description
Extend the API with update and delete operations so clients can edit or remove items.

#### Requirements
Completed program should:

- Define a PUT route at `/items/{item_id}` to update an existing item.
- Define a DELETE route at `/items/{item_id}` to remove an item.
- Return appropriate success responses for update and delete actions.
- Handle cases where the requested item does not exist.

### 🛠️ Explore FastAPI Documentation

#### Description
Use FastAPI's built-in documentation UI to verify your endpoints and view request schemas.

#### Requirements
Completed program should:

- Start the FastAPI app and open the Swagger UI at `/docs`.
- Confirm item routes appear with the correct request and response schemas.
- Use the docs UI or a tool like `curl` to test at least one endpoint.
