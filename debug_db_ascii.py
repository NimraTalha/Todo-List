"""
Debug script to test database connection
"""
import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from src.backend.models import User

# Load environment
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("[ERROR] DATABASE_URL not found in .env file")
    print("Contents of .env file:")
    try:
        with open(".env", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No .env file found")
    exit(1)

print(f"[OK] DATABASE_URL found: {DATABASE_URL[:50]}...")

try:
    # Create engine
    print("Attempting to create database engine...")
    engine = create_engine(DATABASE_URL)

    # Test connection
    print("Testing database connection...")
    with engine.connect() as conn:
        print("[OK] Database connection successful!")

    # Try to create tables
    print("Attempting to create tables...")
    SQLModel.metadata.create_all(engine)
    print("[OK] Tables created successfully!")

    # Test creating a session
    print("Testing session creation...")
    with Session(engine) as session:
        print("[OK] Session creation successful!")

    print("\n[SUCCESS] Database setup is working correctly!")

except Exception as e:
    print(f"[ERROR] Database error: {e}")
    import traceback
    traceback.print_exc()