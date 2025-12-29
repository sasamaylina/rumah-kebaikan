from datetime import datetime
from models.db import get_db_connection

class DonationModel:
    def __init__(self):
        pass

    def create(self, user_id, campaign_id, jumlah, message=''):
        """Create a new donation"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO donations (user_id, campaign_id, jumlah, message, created_at) 
                         VALUES (%s, %s, %s, %s, %s)"""
                created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(sql, (user_id, campaign_id, jumlah, message, created_at))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()
    
    def getAll(self):
        """Get all donations with user and campaign info (for admin)"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """SELECT d.*, u.username, c.nama as campaign_nama 
                         FROM donations d
                         JOIN users u ON d.user_id = u.id
                         JOIN campaigns c ON d.campaign_id = c.id
                         ORDER BY d.created_at DESC"""
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()
    
    def getByUserId(self, user_id):
        """mengambil satu donasi berdasarkan user id untuk riwayat donasi"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """SELECT d.*, c.nama as campaign_nama 
                         FROM donations d
                         JOIN campaigns c ON d.campaign_id = c.id
                         WHERE d.user_id = %s
                         ORDER BY d.created_at DESC"""
                cursor.execute(sql, (user_id,))
                return cursor.fetchall()
        finally:
            connection.close()
    
    def getByCampaignId(self, campaign_id):
        """Get donations for a specific campaign"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """SELECT d.*, u.username 
                         FROM donations d
                         JOIN users u ON d.user_id = u.id
                         WHERE d.campaign_id = %s
                         ORDER BY d.created_at DESC"""
                cursor.execute(sql, (campaign_id,))
                return cursor.fetchall()
        finally:
            connection.close()
    
    def getTotalDonations(self):
        """Get total donation amount"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT SUM(jumlah) as total FROM donations"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['total'] if result and result['total'] else 0
        finally:
            connection.close()
    
    def countDonors(self):
        """menghitung berapa banyak donatur"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT COUNT(DISTINCT user_id) as total FROM donations"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['total'] if result else 0
        finally:
            connection.close()
    
    def countAll(self):
        """menghitung jumlah donasi"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT COUNT(*) as total FROM donations"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['total'] if result else 0
        finally:
            connection.close()
