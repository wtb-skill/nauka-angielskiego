from app_v2 import app, db
from app_v2.models import Word


if __name__ == "__main__":
    with app.app_context():
        # Delete all records from the Word table
        Word.query.delete()

        # Commit the changes to the database
        db.session.commit()
