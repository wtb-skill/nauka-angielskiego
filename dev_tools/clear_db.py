# /dev_tools/clear_db.py
from app_v2 import app, db


def drop_all_tables():
    with app.app_context():
        db.drop_all()


def create_all_tables():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    """DELETE ALL DATA FROM THE DB  /// DEVELOPMENT TOOL"""
    drop_all_tables()
    create_all_tables()
