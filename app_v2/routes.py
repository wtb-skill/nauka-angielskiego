# app_v2/routes

from flask import render_template, request, redirect, url_for, flash, session
from app_v2 import app, db
from app_v2.models import BaseWords, Word
import random


def first_run():
    count_in_hand = Word.query.filter_by(placement='in_hand').count()
    check = count_in_hand != 10
    return check


@app.route('/')
def initialise():
    """Initiates the first run of the application by putting 10 new words in hand."""
    if first_run():
        # Fetch all words with 'to_learn' placement
        words_to_learn = Word.query.filter_by(placement='to_learn').all()

        # Shuffle the words list to select random words
        random.shuffle(words_to_learn)

        # Update the placement of the first 10 fetched random words
        for word in words_to_learn[:10]:
            word.placement = 'in_hand'

        # Commit the changes to the database
        db.session.commit()

    return render_template("initialise.html")


@app.route('/hand')
def hand():
    words_in_hand = Word.query.filter_by(placement='in_hand').all()

    return render_template("hand.html", words=words_in_hand)


@app.route('/mastered')
def mastered():
    words_mastered = Word.query.filter_by(placement='mastered').all()

    return render_template("mastered.html", words=words_mastered)


@app.route('/quiz_result')
def quiz_result():
    session['current_word_index'] = 0

    return render_template("quiz_result.html")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    words_in_hand = Word.query.filter_by(placement='in_hand').all()
    current_word_index = session.get('current_word_index', 0)
    current_word = words_in_hand[current_word_index]

    if request.method == 'POST':
        translation = request.form['translation']
        handle_translation(translation, current_word)

        session['current_word_index'] = current_word_index + 1

        if current_word_index + 1 < len(words_in_hand):
            return redirect('/quiz')
        else:
            return redirect('/quiz_result')

    return render_template("quiz.html", word=current_word, index=current_word_index, total_words=len(words_in_hand))


def handle_translation(translation, current_word):
    if current_word.stars < 3:
        handle_low_stars_translations(translation, current_word)
    else:
        handle_high_stars_translations(translation, current_word)


def handle_low_stars_translations(translation, current_word):
    if translation == current_word.pol:
        current_word.stars += 1
        db.session.commit()
        flash('Correct!', 'success')
    else:
        current_word.stars -= 1
        current_word.stars = max(current_word.stars, 0)
        db.session.commit()
        flash('Incorrect. Try again!', 'danger')


def handle_high_stars_translations(translation, current_word):
    if translation == current_word.eng:
        current_word.stars += 1
        db.session.commit()
        flash('Correct!', 'success')
    else:
        current_word.stars -= 1
        current_word.stars = max(current_word.stars, 0)
        db.session.commit()
        flash('Incorrect. Try again!', 'danger')