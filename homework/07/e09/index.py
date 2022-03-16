""" 
Module that has function that modifys index.html page
"""
from flask import Flask, render_template, request
from repository import save_to_database, read_database
from validation import is_name
from string_helper import csv_to_list

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    """ 
    Renders index.html template and if reguest method
    is POST, checks if given names are real names and
    if they are, saves them to the database.txt 

    Parameters
    ----------
    fname : `string`
        given firstname in form
    lname : `string`
       given lastname in form
    x : `bool`
        boolean to check if name is a real name
    y : `bool`
        boolean to check if name is a real name
    db_string : `string`
        database.txt in string form
    
    Returns
    -------
    return :
        returns index.html render template with 
        updated database if method is POST
    """
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        print(fname)
        print(lname)
        x = is_name(fname)
        y = is_name(lname)
        if x and y:
            save_to_database(fname, lname)
    db_string = read_database()
    return render_template('index.html', names = csv_to_list(db_string))

if __name__ == "__main__":
    app.run(debug=True)