from app import app
from app.ac.getraces import Races
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/races')
def get_races():
    races = Races.get_races()
    return render_template('raceTiles.html',
                           races=races)
