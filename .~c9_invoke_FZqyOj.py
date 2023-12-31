from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
import calendar


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class ToDo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	starttime = db.Column(db.String(128), nullable=False)
	site = db.Column(db.String(128), nullable=False)
	content = db.Column(db.String(128), nullable=False)
	nunber = db.Column(db.String(128), nullable=False)
	time = db.Column(db.String(128), nullable=False)
	weight = db.Column(db.String(128), nullable=False)


@app.route("/")
def hello_world():
    #f = open('cal.txt','w')
    #f.write(calendar.calendar(2023,c=12,m=1))
    #f.close
    c =  open('cal.txt','r')
    c1 = c.readlines()
    c.close

    x = []
    y = [41,42,43,44,45,46,47,48,49,50,51,52,53]
    a = 40
    b = 0
    for i in c1:
        c = i.split()
        d = len(c)
        e = 7-d
        if "28" not in c and "29" not in c and "30" not in c and "31" not in c and "1" not in c and d == 1:
            c.pop(0)
            c.insert(0,str(b)+"月")
            b+=1
        if d == 0:
            a += 1
            c.insert(0,str(a))
        if 0 < d < 7 and "1" in c:
            for i in range(e):
                c.insert(0,"×")

        f = " ".join(c)
        x.append(f)
    b = "\n".join(x)
    f = open('cal(a).txt','w')
    f.write(b)
    f.close

    x.append("53")
    v = []
    w = []
    d = -1
    #x = [1,2,3,4]
    #y = [41]
    e = len(x)
    for i in y:
        for j in range(e):
            v.append(x[0])
            x.pop(0)
            d += 1
            if str(i) not in v:
                w.insert(d,v[-1])
            else:
                h = "\n".join(w)
                f = open('cal'+str(i-41)+'.txt','w')
                f.write(h)
                f.close
                w = []
                d = -1
                break
    
    d =  open('day.txt','r')
    d13 = d.readlines()
    d.close
    
    d =  open('day1.txt','r')
    d14 = d.readlines()
    d.close
    
    d =  open('dbid.txt','r')
    d15 = d.readlines()
    d.close
    
    
    item=["トレーニング", "食事"]
    d =  open('tra.txt','r')
    kinds = d.readlines()
    d.close
    
    d =  open('cal11.txt','r')
    g12 = d.readlines()
    d.close
    
    
    
    #x2 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
    d0=d13[0]
    d01=d14[0]
    d02=[]
    
    x0 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    z=0
    for i in x0:
        z+=1
        if i == d01:
            d =  open('cal'+str(z)+'.txt','r')
            d1 = d.readlines()
            d.close
            d02.append(str(z)+"月")
    
    x3 = [d1]
    
    x=[]
    data = ToDo.query.all()
    for d in data:
        x.append(d.id)

    y=[]
    for i in x:
        y.append(str(i))
    
        
    if kinds[0] == "トレーニング":
        z=str(1) + d15[0]
        x0=[s for s in y if str(z) in s]
        if len(x0) == 0:
            z=str(1) + d15[0] + str(1)
            x0.append(int(z))
        else:
            z=str(1) + d15[0] + str(len(x0) + 1)
            x0.append(int(z))
       
            
    if kinds[0] == "食事":
        z=str(2) + d15[0]
        x0=[s for s in y if str(z) in s]
        if len(x0) == 0:
            z=str(2) + d15[0] + str(1)
            x0.append(int(z))
        else:
            z=str(2) + d15[0] + str(len(x0) + 1)
            x0.append(int(z))
    
    z0=[int(z)]
    
    x1=[]
    for i in x0:
        x1.append(int(i))
    
    a = -1
    b = 0
    for i in x1:
        a+=1
        if i == int(z):
            b+=1
            if b == 2:
                x1.pop(a)
                #x1.pop(-1)
                x1m=str(max(x1))
                x1mm=int(x1m[-1])
                z=x1m[:-1]+str(x1mm+1)
                x1.append(int(z))
    z0=[int(z)]
    
                
    x2=[]   
    for i in x1:
        for j in data:
            if i == j.id:
                x2.append(j)
        for j in z0:
            if i == j:
                x2.append(j)
    
    x5=[]
    for i in range(1,32):
        x5.append(str(i))
    
    a=["Mo","Tu","We","Th","Fr","Sa","Su"]
    a.append(d02[0])
    
    tore=["トレーニング"]
    
    x4 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    
    return render_template("cal.html",a=a, x3=x3, x4=x4, x5=x5,d0=d0, d01=d01, d15=d15, item=item, kinds=kinds,x0=x0, tore=tore, x1=x1, x2=x2, y=y, z0=z0, data=data,g12=g12)

    
@app.route("/result0", methods=["POST"])
def hello0():
    name = request.form["a"]
    f = open('tra.txt','w')
    f.write(name)
    f.close
    
    return redirect(url_for('hello_world'))


@app.route("/result", methods=["POST"])
def hello():
    name = request.form["a"]
    f = open('day.txt','w')
    f.write(name)
    f.close
    
    name1 = request.form["b"]
    f = open('day1.txt','w')
    f.write(name1)
    f.close
    
    x1 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    z=0
    a=0
    for i in x1:
        z+=1
        if i == name1:
            f = open("dbid.txt", "w")
            f.write(str(z))
            f.write(name)
            f.close()
    
    
    #x3=[d1]
    return redirect(url_for('hello_world'))

@app.route("/result1", methods=["POST"])
def hell():
    name = request.form["c"]
    d =  open('tra.txt','r')
    kinds = d.readlines()
    d.close
    tore = ["トレーニング"]
    return render_template("cal3.html", name=name, kinds=kinds, tore=tore)


a=0
@app.route("/result2", methods=["POST"])
def hel():
    name = request.form["a"]
    name1 = request.form["b"]
    name2 = request.form["c"]
    name3 = request.form["d"]
    name4 = request.form["e"]
    name5 = request.form["f"]
    name0 = request.form["g"]

    
    new_todo = ToDo(id = name0, starttime=name, site=name1, content=name2, nunber=name3, time=name4, weight=name5)
    db.session.add(new_todo)
    db.session.commit()
    
    
    return redirect(url_for('hello_world'))
    

@app.route('/del_todo/<int:id>')
def del_todo(id):
	del_data = ToDo.query.filter_by(id=id).first()
	db.session.delete(del_data)
	db.session.commit()
	return redirect(url_for('hello_world'))
        

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
    app.debug = True