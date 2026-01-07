"""
API Test script to verify the backend endpoints
"""
import requests
import threading
import time
import subprocess
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def start_server():
    """Start the backend server in a subprocess"""
    import uvicorn
    from src.backend.main import app

    # Run the server in a separate thread
    def run_server():
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(2)  # Give the server time to start
    return server_thread

def test_api_endpoints():
    """Test the basic API endpoints"""
    base_url = "http://localhost:8000"

    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("[OK] Health endpoint working")
        else:
            print(f"[ERROR] Health endpoint failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"[ERROR] Could not connect to server: {e}")
        return False

    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("[OK] Root endpoint working")
        else:
            print(f"[ERROR] Root endpoint failed with status {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Root endpoint test failed: {e}")

    # Test API endpoints (these will fail due to auth, but should return 401, not 404)
    try:
        response = requests.get(f"{base_url}/api/tasks")
        if response.status_code in [401, 403]:  # Expected due to missing auth
            print("[OK] Tasks endpoint exists (auth required)")
        elif response.status_code == 404:
            print("[ERROR] Tasks endpoint not found")
            return False
        else:
            print(f"[INFO] Tasks endpoint returned {response.status_code} (expected 401 for auth)")
    except Exception as e:
        print(f"[ERROR] Tasks endpoint test failed: {e}")

    return True

if __name__ == "__main__":
    print("Testing API Endpoints...")
    print("=" * 40)

    # Start the server in the background
    print("Starting server...")
    server_thread = start_server()

    # Give a bit more time for server to fully start
    time.sleep(3)

    # Test the endpoints
    success = test_api_endpoints()

    print("\n" + "=" * 40)
    if success:
        print("[OK] API endpoints are accessible!")
        print("Note: Authentication endpoints would require valid JWT tokens")
    else:
        print("[ERROR] API endpoints have issues")

    print("\nServer is running in the background. Press Ctrl+C to stop.")