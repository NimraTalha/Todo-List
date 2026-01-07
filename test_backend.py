"""
Test script to verify the backend implementation
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_backend_imports():
    """Test that all backend modules can be imported without errors"""
    try:
        from src.backend.models import User, Task, TaskCreate, TaskUpdate, TaskRead
        print("[OK] Models imported successfully")

        from src.backend.db import get_session, engine
        print("[OK] Database module imported successfully")

        from src.backend.middleware.jwt import jwt_middleware
        print("[OK] JWT middleware imported successfully")

        from src.backend.routes.tasks import router
        print("[OK] Task routes imported successfully")

        from src.backend.main import app
        print("[OK] Main app imported successfully")

        print("\n[OK] All backend modules imported successfully!")
        return True

    except Exception as e:
        print(f"[ERROR] Error importing backend modules: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_environment():
    """Test that environment variables are properly loaded"""
    from dotenv import load_dotenv
    import os

    load_dotenv()

    required_vars = ['BETTER_AUTH_SECRET', 'DATABASE_URL']
    missing_vars = []

    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)

    if missing_vars:
        print(f"[ERROR] Missing environment variables: {missing_vars}")
        return False
    else:
        print("[OK] All required environment variables are set")
        print(f"[OK] BETTER_AUTH_SECRET is set (length: {len(os.getenv('BETTER_AUTH_SECRET'))})")
        print(f"[OK] DATABASE_URL is set (masked: {'*' * min(20, len(os.getenv('DATABASE_URL', '')))})")
        return True

if __name__ == "__main__":
    print("Testing Backend Implementation...")
    print("=" * 40)

    env_ok = test_environment()
    imports_ok = test_backend_imports()

    print("\n" + "=" * 40)
    if env_ok and imports_ok:
        print("[OK] Backend implementation is ready!")
    else:
        print("[ERROR] Backend implementation has issues")
        sys.exit(1)