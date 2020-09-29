from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:password@localhost/quotes'
#Course-db
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://kutylncrmosvvrvif:56786171441e668e08b0b5bda470a3673e6e879f94466b5e7865eb9ad18268c1f807c3@ec2-54-75-231-215.eu-west-1.compute.amazonaws.com:5432/d7aofkhqpvufo2mq'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://tzwmlmpkdkliuh:f848bd744b405a3fbe8eafe3f1a24c9e5a7f1c14e2aa3bee67e889dc900c26af@ec2-54-243-67-199.compute-1.amazonaws.com:5432/dbvkie13pqfn1l'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

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
