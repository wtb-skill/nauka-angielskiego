import json
from app_v2 import app, db
from app_v2.models import BaseWords


# Create the Flask app context
with app.app_context():
    # Read JSON file
    with open('../VocabularyData/3000-Most-Common-English-Words.json', 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        new_word = BaseWords(eng=item['ENG'], pol=item['PL'], stars=item['stars'])
        db.session.add(new_word)

    db.session.commit()


# Create SQLite database
# conn = sqlite3.connect('english-polish-app.db')
# cursor = conn.cursor()