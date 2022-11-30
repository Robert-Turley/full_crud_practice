from flask import Flask, render_template
from models.wizard import Wizard

app = Flask(__name__)

@app.route('/')
def index():

    wizards = Wizard.get_all()

    return render_template("index.html", wizards=wizards)

if __name__ == "__main__":
    app.run(debug=True)

