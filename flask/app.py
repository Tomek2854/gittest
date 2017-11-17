# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

# lista pytań
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
    {
    'pytanie': 'Kto był głupcem w diablo II, to:',
    'odpowiedzi': ['Tyrael', 'Elziks', 'Ormus'],
    'odpok': 'Tyrael'},
    {
    'pytanie': 'Dobry ziomek ze starego obozu , to:',
    'odpowiedzi': ['Diego', 'Thorus', 'Świstak'],
    'odpok': 'Diego'},
    {
    'pytanie': 'Ile złotych chciał żebrak od księciunia, to:',
    'odpowiedzi': ['2zł', '1zł', '5zł'],
    'odpok': '2zł'},
]


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('index'))

    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)


@app.route('/')
def inde():
    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)


@app.route('/kontakt')
def xddd():
    return 'Cześć, tu Python! Zapłać złotem lub spadaj!!!'


if __name__ == '__main__':
    app.run(debug=True)
