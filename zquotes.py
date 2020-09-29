from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:postgres@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data_test.sqlite')

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))
	



   	  #else:
		 #return render_template('quotes.html')
