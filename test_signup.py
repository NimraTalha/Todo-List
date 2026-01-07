"""
Test script to verify signup functionality
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.backend.main import app
from fastapi.testclient import TestClient

# Create test client
client = TestClient(app)

print("Testing signup with a valid short password...")

# Test signup with a short password
response = client.post("/api/auth/signup", json={
    "email": "test@example.com",
    "name": "Test User",
    "password": "shortpass123"
})

print(f"Signup response status: {response.status_code}")
print(f"Signup response: {response.text}")

if response.status_code == 200:
    data = response.json()
    token = data.get("access_token")
    print(f"\nReceived JWT token: {token[:50]}..." if token else "No token received")

    print("\nTesting protected endpoint with token...")
    # Test accessing protected endpoint with the token
    headers = {"Authorization": f"Bearer {token}"}
    response2 = client.get("/api/tasks", headers=headers)
    print(f"Tasks response status: {response2.status_code}")
    print(f"Tasks response: {response2.text}")
else:
    print("\nSignup failed, checking if user already exists...")
    # Test signin
    response_signin = client.post("/api/auth/signin", json={
        "email": "test@example.com",
        "password": "shortpass123"
    })
    print(f"Signin response status: {response_signin.status_code}")
    print(f"Signin response: {response_signin.text}")