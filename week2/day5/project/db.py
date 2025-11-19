import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
    Returns a psycopg connection to the Neon database.
    """
    # Load credentials from environment variables
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_PORT = os.getenv("DB_PORT")

    # Extract Neon endpoint ID (required for SNI)
    endpoint_id = DB_HOST.split('.')[0]

    # Build connection URI
    DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        f"?sslmode=require&options=endpoint%3D{endpoint_id}"
    )

    # Return the connection
    return psycopg.connect(DATABASE_URL)

# Example usage
if __name__ == "__main__":
    conn = get_connection()
    print("Connection successful!")

    # Example: run a query
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        print("PostgreSQL version:", cur.fetchone()[0])

    conn.close()
