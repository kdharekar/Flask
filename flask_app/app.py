from flask import Flask,render_template,request, redirect
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///kd.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow )

    def __repr__(self):
        return f"{self.sno} -- {self.title}"


@app.route('/',methods=['GET','POST'])
def helloWorld():
    #return "Hello World !! kd"
    if(request.method == 'POST'):
        print("aa")
        return redirect("/products")
    return render_template("home.html")



@app.route('/show')
def show():
    alltodo = Todo.query.all()
    print(alltodo)
    #return "this is response"
    return render_template(home.html)

@app.route('/products', methods=['GET','POST'])
def products():
    if(request.method=='POST'):
        desc = request.form["desc"]
        title = request.form["title"]
        
        todo = Todo(title=title,desc= desc)
        db.session.add(todo)
        db.session.commit()
    #todo = Todo(title = "my todo",desc = "start investing in stocks man")
   
    alltodo = Todo.query.all()
    return render_template('index.html',alltodo=alltodo)
    #return "products !! kd"

if(__name__ == "__main__"):
    app.run(debug=True)
