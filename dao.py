import sqlite3

DATABASE = 'hockey.sqlite3'

def get_db_connection():
    return sqlite3.connect('hockey.sqlite3')

def get_chart_dao(chart_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT coordinates FROM charts WHERE ROWID = :chart_id', {'chart_id': chart_id})
    coordinates = c.fetchone()[0]
    conn.close()

    return coordinates

def save_chart_dao(chart_name, chart_date, shot_coordinates):
    chart_object = {
        'chart_name': chart_name,
        'chart_date': chart_date,
        'shot_coordinates': shot_coordinates
    }

    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO charts VALUES (:chart_name, :chart_date, :shot_coordinates)', chart_object)
    last_row_id = c.lastrowid
    conn.commit()
    conn.close()

    return last_row_id
