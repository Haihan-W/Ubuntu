from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #'Import database function to create DB'

app=Flask(__name__)

#Create DB configuration
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/whh/Ubuntu/task2-Flask-todolist/todo.db' #location of the DB in PC, note: I installed sqlite in PC. Note: After this, need to create todo.db in that directory.

#create a single class for SQLalchemy
db=SQLAlchemy(app) #initiate SQLAlchemy
class Todo(db.Model):
     #create fields in DB
    id = db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(200)) #upper limit=200 char
    complete=db.Column(db.Boolean) #True or False, we want once submit item and it will turn from False to True

@app.route('/') #this is the website link(route) to the webpage
def index():
	todos=Todo.query.filter_by(complete=False).all() #to bring all incompleted BE items in DB to front end,see todos in next line
	completed=Todo.query.filter_by(complete=True).all()
	return render_template('index.html', incomplete = todos, completeditems=completed) #incomplete/completeditems come from index.html, todos/completed are the variables named above, this step will pass todos/completed above from BE Todo.db to FE index.html

@app.route('/add',methods=['POST']) #By this, I created another route to lead to a different page-- a subroute'/add' #Note: 'post' method is only used for submitting a form with a submit button 
def add():
    #add new submitted items to db
    todo=Todo(text=request.form['todoitem'],complete=False) #submittd item 'text' is from whatever you typed and submitted in the webpage. #Here initiated an instance of the Todo class
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index')) #After added item to DB, redirect FE subroute '/add' to FE URL from index(), note: index() is under @app.route('/')

@app.route('/complete/<ids>') #variable 'ids' is created!!!!!!This 'ids' will be referred by hyperlink href in index.html, from there, todo.id will be passed to ids and passed here and passed to the complete function below.
def complete(ids): #purpose: to update the BE DB, mark completed items as complete. When you click the hyperlink 'mark as complete', it will go to this route and finish this complete function and change attribute 'complete' of this clicked item as completed
	todo=Todo.query.filter_by(id=int(ids)).first() #first means: because everytime you will only click on hyperlink for one item, so only one item will be passed. I will assume there is no duplicated items with the same id, even if there is, I use first to choose only the first appeared one. 
	todo.complete=True
	db.session.commit()

	return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)


