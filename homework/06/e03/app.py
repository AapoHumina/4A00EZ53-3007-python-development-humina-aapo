import datetime
from htmlhelper import generate_html_page
from flask import Flask

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)


# if url is in root
@app.route("/html_page")
def html_page():
    title = "Date"
    content = datetime.datetime.now()
    page = generate_html_page(title, content)
    return page


# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)
