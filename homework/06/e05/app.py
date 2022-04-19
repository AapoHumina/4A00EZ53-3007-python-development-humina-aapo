from htmlhelper import generate_html_page
from flask import Flask, render_template, request

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)


# if url is in root
@app.route("/bmi")
def bmi_calculator():
    return render_template("bmi.html")


# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)
