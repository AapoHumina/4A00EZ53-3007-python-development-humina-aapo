import random
from htmlhelper import generate_html_page
from flask import Flask

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)


# if url is in root
@app.route("/slot-machine")
def slot_machine():
    title = "SLOT-MACHINE"
    fruit_list = ["static/cherry.png", "static/banana.png", "static/apricot.png"]
    content1 =f"""<img src="{fruit_list[random.randint(0,2)]}"width="300" height="300">"""
    content2 =f"""<img src="{fruit_list[random.randint(0,2)]}"width="300" height="300">"""
    content3 =f"""<img src="{fruit_list[random.randint(0,2)]}"width="300" height="300">"""
    if content1 == content2 and content2 == content3:
        win = "You win"
    else:
        win = ""
    page = generate_html_page(title, content1, content2, content3, win)
    return page


# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)
