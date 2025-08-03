from flask import Flask
from flask import render_template


# Create flask app instance
application = app = Flask(__name__)

# Add secret key
app.config['SECRET_KEY'] = 'afs87fas7bfsa98fbasbas98fh78oizu'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/f')
def f():
    return render_template('f.html')