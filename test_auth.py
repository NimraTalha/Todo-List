"""
Test script to debug the authentication endpoints
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.backend.main import app
from fastapi.testclient import TestClient

# Create test client
client = TestClient(app)

print("Testing authentication endpoints...")

# Test signup
print("\n1. Testing signup...")
try:
    response = client.post("/api/auth/signup", json={
        "email": "test@example.com",
        "name": "Test User",
        "password": "password123"
    })
    print(f"Signup response status: {response.status_code}")
    print(f"Signup response: {response.text}")
except Exception as e:
    print(f"Signup error: {e}")
    import traceback
    traceback.print_exc()

# Test signin
print("\n2. Testing signin...")
try:
    response = client.post("/api/auth/signin", json={
        "email": "test@example.com",
        "password": "password123"
    })
    print(f"Signin response status: {response.status_code}")
    print(f"Signin response: {response.text}")
except Exception as e:
    print(f"Signin error: {e}")
    import traceback
    traceback.print_exc()

print("\n3. Testing task endpoints (should require auth)...")
try:
    response = client.get("/api/tasks")
    print(f"Get tasks response status: {response.status_code}")
    print(f"Get tasks response: {response.text}")
except Exception as e:
    print(f"Get tasks error: {e}")
    import traceback
    traceback.print_exc()