from models.db import get_db_connection

class CampaignModel:
    def __init__(self):
        pass

    def create(self, data):
        """Create a new campaign"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO campaigns (nama, deskripsi, alamat, kebutuhan, terkumpul, is_active) 
                         VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (
                    data['nama'],
                    data.get('deskripsi', ''),
                    data.get('alamat', ''),
                    int(data.get('kebutuhan', 0)),
                    int(data.get('terkumpul', 0)),
                    data.get('is_active', 1)
                ))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()
    
    def getAll(self):
        """Get all campaigns"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM campaigns ORDER BY created_at ASC"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()
    
    def getActive(self):
        """Get only active campaigns"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM campaigns WHERE is_active = 1 ORDER BY created_at ASC"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()
    
    def getById(self, campaign_id):
        """Get campaign by ID"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM campaigns WHERE id = %s"
                cursor.execute(sql, (campaign_id,))
                return cursor.fetchone()
        finally:
            connection.close()
    
    def update(self, campaign_id, data):
        """Update campaign by ID"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """UPDATE campaigns 
                         SET nama=%s, deskripsi=%s, alamat=%s, kebutuhan=%s, terkumpul=%s, is_active=%s
                         WHERE id=%s"""
                cursor.execute(sql, (
                    data['nama'],
                    data.get('deskripsi', ''),
                    data.get('alamat', ''),
                    int(data.get('kebutuhan', 0)),
                    int(data.get('terkumpul', 0)),
                    data.get('is_active', 1),
                    campaign_id
                ))
            connection.commit()
            return True
        finally:
            connection.close()
    
    def updateTerkumpul(self, campaign_id, amount):
        """Add donation amount to campaign's terkumpul"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE campaigns SET terkumpul = terkumpul + %s WHERE id = %s"
                cursor.execute(sql, (amount, campaign_id))
            connection.commit()
            return True
        finally:
            connection.close()

    def delete(self, campaign_id):
        """Delete campaign by ID"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM campaigns WHERE id = %s"
                cursor.execute(sql, (campaign_id,))
            connection.commit()
            return True
        finally:
            connection.close()
    
    def countAll(self):
        """Count total campaigns"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT COUNT(*) as total FROM campaigns"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['total'] if result else 0
        finally:
            connection.close()
    
    def getTotalTerkumpul(self):
        """Get total collected donations across all campaigns"""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT SUM(terkumpul) as total FROM campaigns"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['total'] if result and result['total'] else 0
        finally:
            connection.close()
