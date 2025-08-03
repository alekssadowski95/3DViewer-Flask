from flask import Flask
from flask import render_template, redirect, url_for


# Create flask app instance
application = app = Flask(__name__)

# Add secret key
app.config['SECRET_KEY'] = 'afs87fas7bfsa98fbasbas98fh78oizu'

@app.route('/')
def home():
    return redirect(url_for('viewer', filename = 'base-machine-vise.FCStd'))

@app.route('/viewer/<filename>')
def viewer(filename):
    return render_template('viewer.html', filename = filename)
