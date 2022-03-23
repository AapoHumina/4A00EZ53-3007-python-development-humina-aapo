from flask import Flask, redirect, render_template, request, session, url_for


# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)
app.secret_key = 'jussi'


@app.route("/", methods=["GET","POST"])
def add_product():
    session["cart"] = []
    list = ["Wine", "Energy Drink", "Beer", "Mac Studio"]

    return render_template("index.html", list=list)

@app.route("/item=<item>", methods=["GET","POST"])
def items(item):
    list = ["Wine", "Energy Drink", "Beer", "Mac Studio"]
    shop_cart = session["cart"]
    shop_cart.append(f"{item}")
    session["cart"] = shop_cart
    print(session["cart"])
    return render_template("index.html", list=list)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)