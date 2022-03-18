import os
import random
from flask import Flask, render_template, request, make_response


# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

picFolder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/slot-machine", methods = ["POST", "GET"])
def slot_machine():
    money = request.cookies.get('money')

    button = "PLAY"
    pic0 = os.path.join(app.config['UPLOAD_FOLDER'], '0.png')
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '1.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '2.png')

    a = random.randint(0, 3)
    b = random.randint(0, 3)
    c = random.randint(0, 3)

    if a == 0:
        a = pic0
    elif a == 1:
        a = pic1
    else:
        a = pic2

    if b == 0:
        b = pic0
    elif b == 1:
        b = pic1
    else:
        b = pic2
    
    if c == 0:
        c = pic0
    elif c == 1:
        c = pic1
    else:
        c = pic2

    if a == b and b == c:
        result = "You win 5$"
        money_check = True
    else:
        result = "You lost"
        money_check = False

    if money == None:
        money = 20
    elif money_check:
        money = int(money) + 4
    else:
        money = int(money) - 1 

    if money == 0:
        result = "You lose, play again when you have money :)"
        response = make_response(render_template("index.html", pic0=a, pic1=b, pic2=c, result=result, button=button, money = money))
        response.delete_cookie('money')
    else:
        response = make_response(render_template("index.html", pic0=a, pic1=b, pic2=c, result=result, button=button, money = money))
        response.set_cookie('money', f"{money}")

    return response

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)