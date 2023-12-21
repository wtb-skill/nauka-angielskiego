# app_v2/routes

from flask import render_template, request, redirect, url_for, flash
from app_v2 import app, db


@app.route('/')
def base():
    return render_template("base.html")


@app.route('/hand')
def hand():
    return render_template("hand.html")


@app.route('/mastered')
def mastered():
    return render_template("mastered.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")