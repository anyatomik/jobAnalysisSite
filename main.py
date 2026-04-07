from flask import Flask,render_template, request
from flask_frozen import Freezer
import git
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)


@app.route('/')
def mainn():
    return render_template('index.html')
if __name__ == '__main__':
    freezer.freeze()
    #app.run(debug=True)