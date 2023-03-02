import json
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # build a graphical representation of a hockey rink
    # and return it to the user

    return render_template('create_chart.html')

@app.route('/chart/<int:chart_id>', methods=['GET'])
def show_chart(chart_id):
    # show the chart with the given id, the id is an integer

    # get the coordinates for the given chart_id from the database
    conn = sqlite3.connect('hockey.sqlite3')
    c = conn.cursor()
    c.execute('SELECT coordinates FROM charts WHERE ROWID = :chart_id', {'chart_id': chart_id})
    coordinates = c.fetchone()[0]
    conn.close()

    print(coordinates)
    coordinates_list = json.loads(coordinates)
    print(coordinates_list)

    return render_template('view_chart.html', chart_id=chart_id, coordinates_list=coordinates_list)

@app.route('/clear_chart', methods=['POST'])
def clear_chart():
    # clear the chart

    return redirect('/')


@app.route('/save_chart', methods=['POST'])
def save_chart():

    chart_name = request.form['chart_name']
    chart_date = request.form['chart_date']
    shot_coordinates = request.form['shot_coordinates']

    chart_object = {
        'chart_name': chart_name,
        'chart_date': chart_date,
        'shot_coordinates': shot_coordinates
    }

    # append chart_object to the charts table in the test.db sqlite3 database
    conn = sqlite3.connect('hockey.sqlite3')
    c = conn.cursor()
    c.execute('INSERT INTO charts VALUES (:chart_name, :chart_date, :shot_coordinates)', chart_object)
    last_row_id = c.lastrowid
    conn.commit()
    conn.close()


    return redirect(f'/chart/{last_row_id}')