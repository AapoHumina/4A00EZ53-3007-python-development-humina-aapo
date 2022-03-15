from flask import Flask, render_template, request
from repository import save_to_database
from validation import is_name

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        x = is_name(fname)
        y = is_name(lname)
        if x and y:
            save_to_database(fname, lname)
    return render_template('index.html', name="Jack")

if __name__ == "__main__":
    app.run(debug=True)