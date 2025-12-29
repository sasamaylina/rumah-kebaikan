from datetime import datetime
from models.db import get_db_connection

class UserModel:
    def __init__(self):
        pass

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
        """membuat user baru"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO users (username, email, password, role, created_at) 
                         VALUES (%s, %s, %s, %s, %s)"""
                created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(sql, (username, email, password, role, created_at))
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