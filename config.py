"""
Configuration module for Rumah Kebaikan application.
Loads settings from environment variables for security and flexibility.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class with common settings."""
    
    # Flask Settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'rumah_kebaikan')
    
    # Security Settings
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False').lower() == 'true'
    SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_HTTPONLY', 'True').lower() == 'true'
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')
    
    # CSRF Protection
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None  # No time limit for CSRF tokens
    
    # Application Info
    APP_NAME = os.getenv('APP_NAME', 'Rumah Kebaikan')
    APP_VERSION = os.getenv('APP_VERSION', '1.0.0')


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    TESTING = False
    
    # Override security settings for production
    SESSION_COOKIE_SECURE = True  # Require HTTPS
    
    @classmethod
    def init_app(cls, app):
        """Production-specific initialization."""
        # Ensure SECRET_KEY is set in production
        if cls.SECRET_KEY == 'dev-secret-key-change-in-production':
            raise ValueError(
                'SECRET_KEY must be set in production environment! '
                'Generate a secure key and set it in .env file.'
            )


class TestingConfig(Config):
    """Testing environment configuration."""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env_name=None):
    """
    Get configuration object based on environment name.
    
    Args:
        env_name: Environment name (development, production, testing)
                 If None, uses FLASK_ENV environment variable or defaults to 'development'
    
    Returns:
        Configuration class for the specified environment
    """
    if env_name is None:
        env_name = os.getenv('FLASK_ENV', 'development')
    
    return config.get(env_name, config['default'])
