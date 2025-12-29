"""
User model for managing user data and authentication.
Implements secure password hashing using bcrypt.
"""
from datetime import datetime
from models.db import get_db_connection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class UserModel:
    def __init__(self):
        pass
    
    @staticmethod
    def hash_password(password):
        """
        Hash a password using bcrypt.
        
        Args:
            password (str): Plain text password
            
        Returns:
            str: Hashed password
        """
        return bcrypt.generate_password_hash(password).decode('utf-8')
    
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        Verify a password against its hash.
        Supports both bcrypt hashed passwords and legacy plain text passwords.
        
        Args:
            plain_password (str): Plain text password to verify
            hashed_password (str): Hashed password from database
            
        Returns:
            bool: True if password matches, False otherwise
        """
        # Check if password is bcrypt hashed (starts with $2b$, $2a$, or $2y$)
        if hashed_password and hashed_password.startswith('$2'):
            try:
                return bcrypt.check_password_hash(hashed_password, plain_password)
            except ValueError:
                return False
        else:
            # Legacy plain text password comparison
            # WARNING: This is for migration period only, run db_migration.py!
            return hashed_password == plain_password

    def find_by_username(self, username):
        """mencari user berdasarkan username"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE username = %s"
                cursor.execute(sql, (username,))
                return cursor.fetchone()
        finally:
            connection.close()
    
    def find_by_id(self, user_id):
        """mencari user berdasarkan id"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE id = %s"
                cursor.execute(sql, (user_id,))
                return cursor.fetchone()
        finally:
            connection.close()
    
    def find_by_email(self, email):
        """mencari user berdasarkan email"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE email = %s"
                cursor.execute(sql, (email,))
                return cursor.fetchone()
        finally:
            connection.close()
    
    def create(self, username, email, password, role='donatur'):
        """
        Create a new user with hashed password.
        
        Args:
            username (str): Unique username
            email (str): User email address
            password (str): Plain text password (will be hashed)
            role (str): User role ('admin' or 'donatur'), defaults to 'donatur'
            
        Returns:
            int: ID of the newly created user
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # Hash the password before storing
                hashed_password = self.hash_password(password)
                
                sql = """INSERT INTO users (username, email, password, role, created_at) 
                         VALUES (%s, %s, %s, %s, %s)"""
                created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(sql, (username, email, hashed_password, role, created_at))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()
    
    def countDonors(self):
        """menghitung jumlah donatur"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT COUNT(*) as total FROM users WHERE role = 'donatur'"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['total'] if result else 0
        finally:
            connection.close()
    
    def getAll(self):
        """mengambil semua user"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, username, email, role, created_at FROM users ORDER BY created_at DESC"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()
    
    @staticmethod
    def validate_password_strength(password):
        """
        Validate password strength.
        
        Args:
            password (str): Password to validate
            
        Returns:
            tuple: (bool, str) - (is_valid, error_message)
        """
        if len(password) < 8:
            return False, "Password minimal 8 karakter"
        
        # Check for at least one number or special character (recommended but not enforced strictly)
        # For now, just enforce minimum length
        
        return True, ""