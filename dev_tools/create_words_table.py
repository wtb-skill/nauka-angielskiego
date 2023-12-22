# dev_tools/create_words_table.py

from app_v2 import app, db
from app_v2.models import BaseWords, Word


if __name__ == "__main__":
    with app.app_context():
        # Fetch all BaseWords
        base_words = BaseWords.query.all()

        # Create corresponding Word entries with placement='to_learn'
        words_to_learn = [
            Word(eng=base_word.eng, pol=base_word.pol, stars=base_word.stars, placement='to_learn')
            for base_word in base_words
        ]

        # Add Words to the database
        db.session.bulk_save_objects(words_to_learn)
        db.session.commit()
