from flask_app import app
from flask import render_template, redirect, request, session, flash 
from flask_app.models.wizard import Wizard



@app.route('/')
def index():
    wizards = Wizard.get_all()
    return render_template("index.html", wizards=wizards)

@app.route('/newwizard')
def new_wizard():
    return render_template("newwizard.html")

@app.route('/createwizard', methods=['POST'])
def create_wizard():
    data = {
        "Name" : request.form['name'],
        "Type" : request.form['type'],
        "Power" : request.form['power']
    }
    Wizard.create_one(data)
    return redirect ('/')

@app.route('/viewwizard/<int:wizard_id>')
def view_wizard(wizard_id):
    data = {
        "id":wizard_id
    }
    wizard_from_db = Wizard.get_one(data) 
    return render_template("wizard.html", wizard = wizard_from_db)

@app.route('/updatewizard/<int:wizard_id>')
def update_one(wizard_id):
    
    data = {
        "id": wizard_id
    }
    current_wizard = Wizard.get_one(data)
    return render_template("updatewizard.html", wizard = current_wizard)

@app.route('/changewizard', methods = ['POST'])
def change_one():

    data = {
        "name": request.form["name"], 
        "type": request.form["type"],
        "power": request.form["power"],
        "id": request.form["id"]
    }
    Wizard.update_one(data)
    return redirect(f'/viewwizard/{request.form["id"]}')

@app.route('/deletewizard/<int:wizard_id>')
def delete_one(wizard_id):
    data = {
        "id": wizard_id
    }
    Wizard.delete_one(data)
    return redirect('/')