from flask import Flask ,render_template , request ,session,redirect
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

import json
from datetime import datetime

from flask_sqlalchemy.model import Model

with open('config.json', 'r') as c:
    dargo = json.load(c)["dargo"]

app = Flask(__name__)
app.secret_key = 'amar2490'
app.config['UPLOAD_FOLDER'] = dargo['upload_location']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dargo'
db = SQLAlchemy(app)

class Details(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(40), nullable=False)
    img = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    engine = db.Column(db.String(40), nullable=False)
    power = db.Column(db.String(40), nullable=False)
    torque = db.Column(db.String(40), nullable=False)
    clearence = db.Column(db.String(40), nullable=False)
    mileage = db.Column(db.String(40), nullable=False)
    tank = db.Column(db.String(40), nullable=False)
    gearbox = db.Column(db.String(40), nullable=False)
    height = db.Column(db.String(40), nullable=False)
    length = db.Column(db.String(40), nullable=False)
    width = db.Column(db.String(40), nullable=False)
    weight = db.Column(db.String(40), nullable=False)
    wheelbase = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(12), nullable=False)

class Latest(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    cnamemodel = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    through = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)
class Latestbike(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    cnamemodel = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    through = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)
class Latestcar(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    cnamemodel = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    through = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)
@app.route("/")
def index():
    posts = Latest.query.all()[0:3]
    item = Latestcar.query.all()[0:5]
    item1 = Latestbike.query.all()[0:5]
    return render_template("index.html",posts=posts,item=item,item1=item1)

@app.route("/admin", methods = ['GET','POST'])
def admin():
    if "user" in session and session['user']==dargo['uname']:
        posts = Details.query.all()
        return render_template("dashboard.html", dargo=dargo,posts=posts)
    if request.method=="POST":
        username = request.form.get("uname")
        userpass = request.form.get("pname")
        if username==dargo['uname'] and userpass==dargo['upass']:
            # set the session variable
            session['user']=username
            posts = Details.query.all()
            return render_template("dashboard.html",dargo=dargo,posts=posts)
    return render_template("admin.html")
    
@app.route("/admin/data", methods = ['GET','POST'])
def add():
    if "user" in session and session['user']==dargo['uname']:
        
        if(request.method=='POST'):
            '''Add entry to the database'''
            cname = request.form.get('cname')
            model = request.form.get('model')
            f = request.files['img']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            
            img = f.filename
            price = request.form.get('price')
            engine = request.form.get('engine')
            power = request.form.get('power')
            torque = request.form.get('torque')
            clearence = request.form.get('clearence')
            mileage = request.form.get('mileage')
            tank = request.form.get('tank')
            gearbox = request.form.get('gearbox')
            height = request.form.get('height')
            length = request.form.get('length')
            width = request.form.get('width')
            weight = request.form.get('weight')
            wheelbase = request.form.get('wheelbase')
            entry = Details(cname=cname, model = model,img=img,  price = price,engine=engine,  
            power = power,torque = torque,clearence=clearence,mileage=mileage,tank=tank,gearbox=gearbox,
            height=height,length=length,width=width, weight=weight,wheelbase=wheelbase, date= datetime.now() )
            db.session.add(entry)
            db.session.commit()

        return render_template("add.html")
    return render_template("admin.html")
@app.route("/admin/latest", methods = ['GET','POST'])
def add1():
    if "user" in session and session['user']==dargo['uname']:
        if(request.method=='POST'):
            cnamemodel = request.form.get('model')
            details = request.form.get('details')
            through = request.form.get('through')
            entry = Latest(model=cnamemodel,details=details,through=through, date= datetime.now())
            db.session.add(entry)
            db.session.commit()

            posts = Latest.query.all()
        return render_template("latest.html",dargo=dargo)
    return render_template("admin.html")
@app.route("/admin/latestcar", methods = ['GET','POST'])
def add2():
    if "user" in session and session['user']==dargo['uname']:
        if(request.method=='POST'):
            cnamemodel = request.form.get('model')
            details = request.form.get('details')
        
            through = request.form.get('through')
            entry = Latest(model=cnamemodel,details=details,through=through, date= datetime.now())
            db.session.add(entry)
            db.session.commit()
        return render_template("latestcar.html")
    return render_template("admin.html")
@app.route("/admin/latestbike", methods = ['GET','POST'])
def add3():
    if "user" in session and session['user']==dargo['uname']:
        if(request.method=='POST'):
            cnamemodel = request.form.get('model')
            details = request.form.get('details')
        
            through = request.form.get('through')
            entry = Latest(model=cnamemodel,details=details,through=through, date= datetime.now())
            db.session.add(entry)
            db.session.commit()
        return render_template("latestbike.html")
    return render_template("admin.html")
@app.route("/show", methods = ['GET','POST'])
def show():
    show1 = request.form['model']
    posts = Details.query.filter_by(model=show1).all()

    return render_template("show.html" ,posts=posts)
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/know")
def know():
    return render_template("know.html")
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/admin')
    
app.run(debug=True)
