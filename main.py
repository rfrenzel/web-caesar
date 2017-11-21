from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    marign: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin-area: 10px 0;
                    width: 540px;
                    height: 128px;
                }
            </style>
        </head>
        <body>
            <form method="post">
                <label>Rotate By
                    <input type="text" name="rot" value="0" />
                </label>
                <label>
                    <textarea name="text"></textarea>
                </label>
                <input type="submit" />
            </form>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form 

@app.route("/", methods=['POST'])
def encrypt():
    working_rot = int(request.form['rot'])
    working_text = str(request.form['text'])

    result = rotate_string(working_text,working_rot)
        
    content = "<h1>" + result + "</h1>"

    return content

app.run()
