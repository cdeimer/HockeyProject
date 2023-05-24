from hockey_rink import NHLRink, RinkImage
import matplotlib.pyplot as plt
from dao import get_chart_info
import json
from io import BytesIO

def plot_export(chart_id):
    # get the coordinates for the given chart_id from the database
    coordinates, home_team, away_team = get_chart_info(chart_id)
    coordinates_list = []
    if coordinates:
        coordinates_list = json.loads(coordinates)
        coordinates_list.append([0, 0, 'orange'])

    # scale down each coordinate by 10
    coordinates_list = [[x/10, -y/10, color] for x, y, color in coordinates_list]

    x, y, color = zip(*coordinates_list)

    rink = NHLRink()

    # plot the coordinates using the rink implementation of a matplotlib scatter plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    rink.scatter(x, y, color=color, edgecolor="white", ax=ax)
    ax.set_title(f'{home_team} vs {away_team}')

    # save the plot to a binary buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer