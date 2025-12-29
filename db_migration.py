"""
Database Migration Script for Rumah Kebaikan
Migrates existing plain text passwords to bcrypt hashed passwords.
"""
import pymysql
from flask_bcrypt import Bcrypt
import os

bcrypt = Bcrypt()

# Database configuration - UPDATE THESE FOR PYTHONANYWHERE
# Or set environment variables before running
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'rumahkebaikan.mysql.pythonanywhere-services.com'),
    'user': os.getenv('DB_USER', 'rumahkebaikan'),
    'password': os.getenv('DB_PASSWORD', ''),  # SET THIS!
    'database': os.getenv('DB_NAME', 'rumahkebaikan$rumahdb'),
}

def migrate_passwords():
    """
    Migrate all plain text passwords to bcrypt hashed passwords.
    
    IMPORTANT: This script should only be run ONCE on existing database.
    After migration, all new passwords will be automatically hashed.
    """
    
    print("=" * 60)
    print("Database Password Migration Script")
    print("=" * 60)
    print(f"Connecting to database: {DB_CONFIG['database']} at {DB_CONFIG['host']}")
    
    connection = None
    
    try:
        connection = pymysql.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            cursorclass=pymysql.cursors.DictCursor
        )
        
        print("✓ Database connection successful")
        
        with connection.cursor() as cursor:
            # Get all users with their current passwords
            cursor.execute("SELECT id, username, password FROM users")
            users = cursor.fetchall()
            
            print(f"\nFound {len(users)} users to migrate")
            
            migrated_count = 0
            skipped_count = 0
            
            for user in users:
                user_id = user['id']
                username = user['username']
                current_password = user['password']
                
                # Check if password is already hashed (bcrypt hashes start with $2b$ or $2a$ or $2y$)
                if current_password.startswith('$2') and len(current_password) == 60:
                    print(f"  ⊘ Skipping {username} - already hashed")
                    skipped_count += 1
                    continue
                
                # Hash the plain text password
                hashed_password = bcrypt.generate_password_hash(current_password).decode('utf-8')
                
                # Update the user's password
                cursor.execute(
                    "UPDATE users SET password = %s WHERE id = %s",
                    (hashed_password, user_id)
                )
                
                print(f"  ✓ Migrated {username}")
                migrated_count += 1
            
            # Commit all changes
            connection.commit()
            
            print("\n" + "=" * 60)
            print(f"Migration Complete!")
            print(f"  - Migrated: {migrated_count} users")
            print(f"  - Skipped: {skipped_count} users (already hashed)")
            print(f"  - Total: {len(users)} users")
            print("=" * 60)
            
    except pymysql.Error as e:
        print(f"\n✗ Database error: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False
    finally:
        if connection:
            connection.close()
            print("\n✓ Database connection closed")
    
    return True


def fix_user_roles():
    """
    Fix any empty role values in the database.
    Changes empty string roles to 'donatur'.
    """
    connection = None
    
    print("\n" + "=" * 60)
    print("Fixing User Roles")
    print("=" * 60)
    
    try:
        connection = pymysql.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            cursorclass=pymysql.cursors.DictCursor
        )
        
        with connection.cursor() as cursor:
            # Find users with empty roles
            cursor.execute("SELECT id, username, role FROM users WHERE role = '' OR role IS NULL")
            users = cursor.fetchall()
            
            if users:
                print(f"Found {len(users)} users with empty roles")
                
                for user in users:
                    cursor.execute(
                        "UPDATE users SET role = 'donatur' WHERE id = %s",
                        (user['id'],)
                    )
                    print(f"  ✓ Fixed role for {user['username']}")
                
                connection.commit()
                print(f"\n✓ Fixed {len(users)} user roles")
            else:
                print("✓ All user roles are valid")
        
    except pymysql.Error as e:
        print(f"✗ Database error: {e}")
        return False
    finally:
        if connection:
            connection.close()
    
    return True


if __name__ == '__main__':
    print("\n⚠️  WARNING: This script will modify your database!")
    print("⚠️  Make sure you have backed up your database before proceeding.\n")
    
    response = input("Do you want to continue? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\nStarting migration...\n")
        
        # Run password migration
        success = migrate_passwords()
        
        if success:
            # Fix user roles
            fix_user_roles()
            
            print("\n✓ All migrations completed successfully!")
            print("\nNext steps:")
            print("1. Test login with existing users")
            print("2. Verify new registrations work correctly")
            print("3. Delete this script or keep it for reference")
        else:
            print("\n✗ Migration failed. Please check the error messages above.")
    else:
        print("\nMigration cancelled.")
