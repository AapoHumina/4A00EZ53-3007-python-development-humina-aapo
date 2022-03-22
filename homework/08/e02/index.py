from flask import Flask, redirect, render_template, request, session, url_for


# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)
app.secret_key = 'jussi'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page1", methods=['GET', 'POST'])
def page1():
    """ If username is found from the session, display
    templates/page1.html. Otherwise display templates/login.html"""
    if "user" in session:
        user = session["user"]
        return render_template("page1.html", user = user)
    else:
        #return redirect(url_for("login"))
        real_user = "aapo"
        real_pwd = "123"
        if request.method == "POST":
            user = request.form["name"]
            pwd = request.form["pwd"]
            if user == real_user and real_pwd == pwd:
                session["user"] = user
                #return redirect(url_for("page1"))
                return render_template("page1.html", user = user)
            else:
                msg = "Incorrect username / password"
                return render_template("login.html", check=1, error= msg)
        return render_template("login.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    """ This url called from login.html. if method is POST, Check if given 
    username and password are correct. If so, display page1.html,
    otherwise display error message """
    real_user = "aapo"
    real_pwd = "123"
    if request.method == "POST":
        user = request.form["name"]
        pwd = request.form["pwd"]
        if user == real_user and real_pwd == pwd:
            session["user"] = user
            return render_template("page1.html", user = user)
        else:
            msg = "Incorrect username / password"
            return render_template("login.html", check=1, error= msg)
    else:
        if "user" in session:
            return redirect(url_for("page1"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    """ remove username from session and display login.html """
    session.pop("user", None)
    #return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/page2", methods=['GET', 'POST'])
def page2():
    """ If username is found from the session, display
    templates/page2.html. Otherwise display templates/login.html"""
    if "user" in session:
        user = session["user"]
        return render_template("page2.html", user = user)
    else:
        #return redirect(url_for("login"))
        real_user = "aapo"
        real_pwd = "123"
        if request.method == "POST":
            user = request.form["name"]
            pwd = request.form["pwd"]
            if user == real_user and real_pwd == pwd:
                session["user"] = user
                return render_template("page1.html", user = user)
            else:
                msg = "Incorrect username / password"
                return render_template("login.html", check=1, error= msg)
        return render_template("login.html")

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)