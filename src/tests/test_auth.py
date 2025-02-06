# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
# from app.db.database import get_db
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.db.database import Base
# from app.schemas.auth import Signup
# from app.core.config import settings

# # Use PostgreSQL for testing
# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}_test"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create the test database schema
# Base.metadata.create_all(bind=engine)

# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

# client = TestClient(app)

# def test_signup():
#     response = client.post("/auth/signup", json={
#         "username": "testuser",
#         "email": "testuser@example.com",
#         "password": "testpassword",
#         "full_name": "Test User"
#     })
#     assert response.status_code == 200
#     assert response.json()["username"] == "testuser"
#     assert response.json()["email"] == "testuser@example.com"

# def test_login():
#     response = client.post("/auth/login", data={
#         "username": "testuser",
#         "password": "testpassword"
#     })
#     assert response.status_code == 200
#     assert "access_token" in response.json()
#     assert response.json()["token_type"] == "bearer"

# def test_refresh_access_token():
#     login_response = client.post("/auth/login", data={
#         "username": "testuser",
#         "password": "testpassword"
#     })
#     refresh_token = login_response.json()["refresh_token"]
#     response = client.post("/auth/refresh", headers={"refresh_token": refresh_token})
#     assert response.status_code == 200
#     assert "access_token" in response.json()
#     assert response.json()["token_type"] == "bearer"