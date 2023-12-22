# app_v2/models.py

from app_v2 import db


class BaseWords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng = db.Column(db.String(100), unique=True, nullable=False)
    pol = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer)

    def __repr__(self):
        return f"<Word {self.eng} - {self.pol}>"


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng = db.Column(db.String(100), unique=True, nullable=False)
    pol = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer)
    placement = db.Column(db.String(100))

    def __repr__(self):
        return f"<Word {self.eng} - {self.pol} {'*' * self.stars}>"
    


# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), unique=True, nullable=False)
#     description = db.Column(db.Text)
#     status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
#
#     # Define the relationship with Author
#     authors = db.relationship('Author', secondary=book_authors, backref=db.backref('books', lazy='dynamic'))
#
#     # Define the relationship with Status
#     status = db.relationship('Status', backref='book_status', lazy=True)
#
#     def __repr__(self):
#         return f"<Book {self.title}>"
#
#
# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     surname = db.Column(db.String(100), nullable=False)
#     bio = db.Column(db.Text)
#
#     def __repr__(self):
#         return f"<Author {self.name} {self.surname}>"
#
#
# class Status(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     available = db.Column(db.Boolean, default=True)
#     borrower_name = db.Column(db.String(100))
#     borrowed_date = db.Column(db.String(100))
#
#     def __repr__(self):
#         if self.available:
#             return "<Status: Available>"
#         else:
#             return f"<Status: Borrowed by {self.borrower_name} on {self.borrowed_date}>"
#
# book_authors = db.Table(
#     'book_authors',
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
#     db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
# )