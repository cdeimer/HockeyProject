import json
from flask import Flask, render_template, request, redirect
from dao import get_chart_info, save_chart_dao

app = Flask(__name__)

@app.route('/')
def index():
    """
    Main page of the app where the user can create a new chart
    """

    return render_template('create_chart.html')

@app.route('/chart/<int:chart_id>', methods=['GET'])
def show_chart(chart_id):
    """
    Given a chart id, return the chart to the user
    """

    # get the coordinates for the given chart_id from the database
    coordinates, home_team, away_team = get_chart_info(chart_id)

    coordinates_list = []
    if coordinates:
        coordinates_list = json.loads(coordinates)
    
    return render_template('view_chart.html', chart_id=chart_id, coordinates_list=coordinates_list, home_team=home_team, away_team=away_team)

@app.route('/clear_chart', methods=['POST'])
def clear_chart():
    """
    Clear the chart and return the user to the create chart page
    """

    return redirect('/')


@app.route('/save_chart', methods=['POST'])
def save_chart():
    """
    Save a chart to the database and redirect the user to that chart's page
    """
    # the clear chart button hits this route as well, but we don't want to save the chart
    if 'clear_chart_button' in request.form:
        return redirect('/')
    
    last_row_id = save_chart_dao(request.form)

    return redirect(f'/chart/{last_row_id}')