import sqlite3

DATABASE = 'hockey.sqlite3'

def get_db_connection():
    return sqlite3.connect('hockey.sqlite3')

def get_chart_info(chart_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT coordinates, home_team, away_team FROM charts WHERE ROWID = :chart_id', {'chart_id': chart_id})
    chart_info = c.fetchone()
    conn.close()

    return chart_info

def get_all_charts():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT ROWID AS chart_id, name AS chart_name, date AS chart_date, home_team, away_team FROM charts')
    charts = c.fetchall()
    conn.close()

    return charts

def save_chart_dao(chart_info):

    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO charts VALUES (:chart_name, :chart_date, :shot_coordinates, :home_team, :away_team)', clean_chart_object(chart_info))
    last_row_id = c.lastrowid
    conn.commit()
    conn.close()

    return last_row_id

# replace all values in the object with None if they are falsy
def clean_chart_object(chart_object):
    clean_object = {}
    for key, value in chart_object.items():
        if value:
            clean_object[key] = value
        else:
            clean_object[key] = None

    return clean_object