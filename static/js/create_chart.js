document.getElementById('chart_date').valueAsDate = new Date();

var shot_coordinates = [];

var goal_button = document.getElementById('goal_button');
goal_button.addEventListener("click", function (evt) {
    if (goal_button.classList.contains('active')) {
        goal_button.classList.remove('active');
    } else {
        goal_button.classList.add('active');
    }
});

var undo_button = document.getElementById('undo_button');
undo_button.addEventListener("click", function (evt) {
    if (shot_coordinates.length > 0) {
        shot_coordinates.pop();
        document.getElementById('shot_coordinates').value = JSON.stringify(shot_coordinates);
        var last_shot = document.getElementById('hockey_rink').lastChild;
        document.getElementById('hockey_rink').removeChild(last_shot);
    }
});

var hockey_rink = document.getElementById("hockey_rink");
var pt = hockey_rink.createSVGPoint();
hockey_rink.addEventListener("click", function (evt) {
    pt.x = evt.clientX;
    pt.y = evt.clientY;
    // transform mouse position to svg coordinates
    var cursorpt = pt.matrixTransform(hockey_rink.getScreenCTM().inverse());

    var shot_color = "red";

    //check if the goal button is pressed
    if (document.getElementById('goal_button').classList.contains('active')) {
        shot_color = "green";
        goal_button.classList.remove('active');
    }

    //draw a circle at the click location
    var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttributeNS(null, "cx", cursorpt.x);
    circle.setAttributeNS(null, "cy", cursorpt.y);
    circle.setAttributeNS(null, "r", 7);
    circle.setAttributeNS(null, "fill", shot_color);
    circle.setAttributeNS(null, "stroke", "black");
    hockey_rink.appendChild(circle);

    //add the new coordinates to the shot_coordinates array
    shot_coordinates.push([cursorpt.x, cursorpt.y, shot_color]);
    document.getElementById('shot_coordinates').value = JSON.stringify(shot_coordinates);

});

var home_team_dropdown = document.getElementById('home_team');
home_team_dropdown.addEventListener("change", function (evt) {
    var home_team = home_team_dropdown.value;
    document.getElementById('home_team_logo').setAttributeNS('http://www.w3.org/1999/xlink', 'href', "/static/images/he_logos/" + home_team + ".png");
});

var away_team_dropdown = document.getElementById('away_team');
away_team_dropdown.addEventListener("change", function (evt) {
    var away_team = away_team_dropdown.value;
    document.getElementById('away_team_logo').setAttributeNS('http://www.w3.org/1999/xlink', 'href', "/static/images/he_logos/" + away_team + ".png");
});