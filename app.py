from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # build a graphical representation of a hockey rink
    # and return it to the user

    return render_template('good_index.html')

@app.route('/save_chart', methods=['POST'])
def save_chart():

    chart_name = request.form['chart_name']
    chart_date = request.form['chart_date']
    #shot_coordinates = request.form['shot_coordinates']

    print(f'chart_name: {chart_name}, chart_date: {chart_date}, shot_coordinates: {None}')

    chart_object = {
        'chart_name': chart_name,
        'chart_date': chart_date,
        'shot_coordinates': None
    }

    # append chart_object to the charts table in the test.db sqlite3 database
    conn = sqlite3.connect('hockey.sqlite3')
    c = conn.cursor()
    c.execute('INSERT INTO charts VALUES (:chart_name, :chart_date, :shot_coordinates)', chart_object)
    conn.commit()
    conn.close()


    return render_template('good_index.html')