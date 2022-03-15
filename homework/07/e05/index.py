from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        print(name)
    return render_template('index.html', name="Jack")

if __name__ == "__main__":
    app.run(debug=True)