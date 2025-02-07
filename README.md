# ecommerce-api

This is an e-commerce API built with FastAPI and PostgreSQL, using Docker for containerization.

## Prerequisites

- Docker
- FastAPI
- SQLAlchemy(ORM)
- PostgrSQL
- docker-compose
- Ruff - (formatting and linting)
- JWT
- OAuth2
- uvicorn, starlatte 
<!-- - Docker Compose -->

## Environment variable
```sh
db_username =  
db_password =  
db_hostname =  localhost
db_port = 5432
db_name = 

    # JWT Config
secret_key = 
algorithm = "HS256" 
access_token_expire_minutes = 30

DATABASE_URL="postgresql://postgres:your_password@localhost:5432/template1"

```

### Clone the Repository

```sh
git clone https://github.com/Sagor0078/ecommerce-api.git
cd ecommerce-api
```

### Set Up a Virtual Environment:

```sh
python3 -m venv env
source env/bin/activate
```
### Install Dependencies:

```sh
pip install -r requirements.txt
```

### migrate database

```sh
python migrate.py
```

### Run the Application:

```sh
python run.py
```

## API endpoints

[![Directory docs](img/ecom1.png)](https://github.com/Sagor0078/ecommerce-api)
[![Directory docs](img/ecom1.png)](https://github.com/Sagor0078/ecommerce-api)





## Entities and Relationships

- User has a one-to-many relationship with Cart.
- Cart has a many-to-one relationship with User and a one-to-many relationship with CartItem.
- CartItem has a many-to-one relationship with Cart and Product.
- Product has a one-to-many relationship with CartItem.


## Model-View-Controller (MVC) Architecture
- Model: Defined in models.py using SQLAlchemy ORM.
- View: Defined in the routers directory, where each file contains route handlers for different parts of the application.
- Controller: The logic within the route handlers in the routers directory acts as the controller, managing the interaction between the models and the views.


## Clean Code Architecture

Clean Code Architecture (also known as Clean Architecture) aims to separate the concerns of the application into different layers, making the codebase more maintainable, testable, and scalable. Here is how the Clean Code Architecture applies to this project:

### Layers

1. **Entities**:
   - Represent the core business logic and rules.
   - In this project, entities are defined in the `models.py` file using SQLAlchemy ORM.

2. **Use Cases**:
   - Contain the application-specific business rules.
   - These are typically implemented as services or functions that interact with the entities and perform specific tasks.

3. **Interface Adapters**:
   - Convert data from the format most convenient for the use cases and entities to the format most convenient for external agencies such as databases and web APIs.
   - In this project, the `routers` directory contains the route handlers that act as the interface adapters.

4. **Frameworks and Drivers**:
   - Contain the details of the frameworks and tools used by the application.
   - In this project, FastAPI and SQLAlchemy are the frameworks used for building the API and interacting with the database, respectively.



