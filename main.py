from flask import Flask,render_template, request
from flask_frozen import Freezer
import git
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
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


#@app.route('/')
#def mainn():
@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/anyatomik/jobAnalysisSite')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated successfully', 200
    else:
        return 'Wrong event type', 400

    #vacantions = vacancy.query.all()
    #return render_template('index.html') #vacantions = vacantions

# if __name__ == '__main__':
    # freezer.freeze()
   # app.run(debug=True)