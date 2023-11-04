"""Flask App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask config variables."""

    DBHOST = "schedoomdb"
    DBNAME = "schedoomdb" 
    DBUSER = "schedoomdb" 
    DBUPWD = "schedoomdb" 
    
