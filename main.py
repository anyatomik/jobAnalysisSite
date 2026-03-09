from flask import Flask,render_template
from flask_frozen import Freezer
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

freezer = Freezer(app)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #здесь ссылка на бд
database = SQLAlchemy(app)


class vacancy(database.Model):
    searchGeo = database.Column(database.String)
    salaryRan = database.Coulumn(database.String)
    wrkExp = database.Column(database.String)
    wrkType = database.Column(database.String)
    company = database.Column(database.String)

'''


@app.route('/')
def mainn():

    #vacantions = vacancy.query.all()
    return render_template('index.html') #vacantions = vacantions

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)
