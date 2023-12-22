@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    words_in_hand = Word.query.filter_by(placement='in_hand').all()
    current_word_index = session.get('current_word_index', 0)
    current_word = words_in_hand[current_word_index]

    if request.method == 'POST':
        handle_translation(words_in_hand, current_word_index, current_word)

    current_word = words_in_hand[current_word_index]
    return render_template("quiz.html", word=current_word, index=current_word_index, total_words=len(words_in_hand))


def handle_translation(words, index, current_word):
    translation = request.form['translation']
    if current_word.stars < 3:
        handle_low_stars_translations(translation, current_word)
    else:
        handle_high_stars_translations(translation, current_word)

    update_session_and_redirect(index, len(words))


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


def update_session_and_redirect(current_index, words_count):
    session['current_word_index'] = current_index + 1
    if current_index + 1 < words_count:
        return redirect(url_for('quiz'))
    else:
        return redirect(url_for('quiz_result'))

# OLD BUT WORKING
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    words_in_hand = Word.query.filter_by(placement='in_hand').all()
    current_word_index = session.get('current_word_index', 0)
    current_word = words_in_hand[current_word_index]

    if request.method == 'POST':
        translation = request.form['translation']
        if current_word.stars < 3:
            if translation == current_word.pol:
                current_word.stars += 1
                db.session.commit()
                flash('Correct!', 'success')
            else:
                current_word.stars -= 1
                current_word.stars = max(current_word.stars, 0)
                db.session.commit()
                flash('Incorrect. Try again!', 'danger')
        else:
            if translation == current_word.eng:
                current_word.stars += 1
                db.session.commit()
                flash('Correct!', 'success')
            else:
                current_word.stars -= 1
                current_word.stars = max(current_word.stars, 0)
                db.session.commit()
                flash('Incorrect. Try again!', 'danger')

        session['current_word_index'] = current_word_index + 1  # Update the current index in the session

        if current_word_index + 1 < len(words_in_hand):
            return redirect(url_for('quiz'))
        else:
            return redirect(url_for('quiz_result'))

    current_word = words_in_hand[current_word_index]
    return render_template("quiz.html", word=current_word, index=current_word_index, total_words=len(words_in_hand))


# WORKS:
# @app.route('/quiz', methods=['GET', 'POST'])
# def quiz():
#     words_in_hand = Word.query.filter_by(placement='in_hand').all()
#     current_word_index = session.get('current_word_index', 0)
#     current_word = words_in_hand[current_word_index]
#
#     if request.method == 'POST':
#         translation = request.form['translation']
#         handle_translation(translation, current_word)
#
#         session['current_word_index'] = current_word_index + 1
#
#         if current_word_index + 1 < len(words_in_hand):
#             return redirect('/quiz')
#         else:
#             return redirect('/quiz_result')
#
#     return render_template("quiz.html", word=current_word, index=current_word_index, total_words=len(words_in_hand))
#
#
# def handle_translation(translation, current_word):
#     if current_word.stars < 3:
#         if translation == current_word.pol:
#             current_word.stars += 1
#             db.session.commit()
#             flash('Correct!', 'success')
#         else:
#             current_word.stars -= 1
#             current_word.stars = max(current_word.stars, 0)
#             db.session.commit()
#             flash('Incorrect. Try again!', 'danger')
#     else:
#         if translation == current_word.eng:
#             current_word.stars += 1
#             db.session.commit()
#             flash('Correct!', 'success')
#         else:
#             current_word.stars -= 1
#             current_word.stars = max(current_word.stars, 0)
#             db.session.commit()
#             flash('Incorrect. Try again!', 'danger')