"""
Database connection module for Rumah Kebaikan.
Handles MySQL database connections using environment-based configuration.
"""
import pymysql
from config import get_config

# Load configuration
config = get_config()


def get_db_connection():
    """
    Create and return a MySQL database connection.
    
    Uses configuration from environment variables loaded via config module.
    
    Returns:
        pymysql.Connection: Database connection object with DictCursor
        
    Raises:
        pymysql.Error: If connection fails
    """
    try:
        connection = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8mb4',
            autocommit=False
        )
        return connection
    except pymysql.Error as e:
        print(f"Database connection error: {e}")
        raise
