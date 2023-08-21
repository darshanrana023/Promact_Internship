from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#WSGI Application(Web Sourxe Gateway Interface)
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    
def __repr__(self) -> str:
    return f"{self.sno}-{self.title}"
       

#Decorators
@app.route('/')
def hello():
    todo=Todo(title='First To do', desc='This is 1st description')
    db.session.add(todo)
    db.session.commit()
    return "Hello World!"

@app.route('/products')
def product():
    return "This is products page that i made"

# By using render_template we can render html files that is in templates folder
@app.route('/temp')
def temp():
    return render_template('index.html')

# Must require to run the program 
#without this proragm not run 
if __name__ == "__main__":
   app.run()
#if we want to add port then add port=8000in app.run()