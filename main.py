from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {name="text"
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {name="rot"
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form>
       <form action="/add" method="post">
        <label for="new-movie">
            Rotate by
            <input type="text" id="rot" name="rot"/>
            
        </label>
        <input type="submit" value="Add It"/>
    </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form

app.run()
