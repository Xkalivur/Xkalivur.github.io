<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>

        <h1 style="text-align:center;"><br><br><br><br><br><br>Join room</h1><br>

        <p class="centre_text">Your name: <input type="text" id="name"></p>
        <p class="centre_text">Room code: <input type="text" id="code"></p>
        <button class="centre roombutton" onclick="window.location.href='rooms.html';">Room list</button> 

    </body>
</html>
