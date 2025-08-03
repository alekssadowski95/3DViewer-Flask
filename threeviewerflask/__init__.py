from flask import Flask
from flask import render_template


# Create flask app instance
application = app = Flask(__name__)

# Add secret key
app.config['SECRET_KEY'] = 'afs87fas7bfsa98fbasbas98fh78oizu'

@app.route('/viewer/<filename>')
def viewer(filename):
    return render_template('viewer.html', filename = filename)
