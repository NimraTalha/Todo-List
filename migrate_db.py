"""
Database migration script to add missing columns
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlmodel import SQLModel

# Load environment
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("[ERROR] DATABASE_URL not found in .env file")
    exit(1)

print(f"[INFO] Connecting to database...")

try:
    # Create raw engine for DDL operations
    engine = create_engine(DATABASE_URL)

    # Check if users table exists
    with engine.connect() as conn:
        # Check if hashed_password column exists
        result = conn.execute(text("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'users' AND column_name = 'hashed_password'
        """))

        if result.fetchone():
            print("[INFO] hashed_password column already exists")
        else:
            print("[INFO] Adding hashed_password column to users table...")
            # Add the hashed_password column
            conn.execute(text("ALTER TABLE users ADD COLUMN hashed_password VARCHAR(255)"))
            conn.commit()
            print("[SUCCESS] Added hashed_password column")

        # Verify the column exists now
        result = conn.execute(text("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'users' AND column_name = 'hashed_password'
        """))

        if result.fetchone():
            print("[SUCCESS] Column verification passed")
        else:
            print("[ERROR] Column was not added successfully")

    print("\n[SUCCESS] Database migration completed!")

except Exception as e:
    print(f"[ERROR] Migration failed: {e}")
    import traceback
    traceback.print_exc()