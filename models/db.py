import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='rumah_kebaikan',
        cursorclass=pymysql.cursors.DictCursor
    )
