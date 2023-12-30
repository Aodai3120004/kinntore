from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
import calendar
import datetime


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
def LoginScreen():
    
    return render_template("login.html")





@app.route("/login", methods=["POST"])
def login():
    user_id = request.form["user_id"]
    password = request.form["password"]
    
    f =  open('UserName.txt','r')
    user_data = f.readlines()
    f.close
    
    AcountNumber=0
    for i in user_data:
        AcountNumber+=1
        if i[:-1] == str(user_id) + str(password):
            return redirect(url_for("hello_world", int_params=str(AcountNumber)))
    
    
    return render_template("login.html")
    



@app.route("/NewAcount")
def new():
    return render_template("NewAcount.html")

@app.route("/CreateAcount", methods=["POST"])
def Create():
    user_id = request.form["user_id"]
    password = request.form["password"]
    
    
    
    f =  open('UserName.txt','r')
    user_data = f.readlines()
    f.close

    
    for i in user_data:
        if i[:2] == str(user_id) + str(password):
            return redirect(url_for("LoginScreen0"))
            
    
    day =  open('day.txt','a')
    day.write(str(1) + "\n")
    day.close
    
    day1 =  open('day1.txt','a')
    day1.write("１月" + "\n")
    day1.close
    
    dbid =  open('dbid.txt','a')
    dbid.write(str(11) + "\n")
    dbid.close
    
    tra =  open('tra.txt','a')
    tra.write(str("トレーニング") + "\n")
    tra.close
            
    f =  open('UserName.txt','a')
    f.write(str(user_id) + str(password) + "\n")
    f.close
    
    time30 =  open('test.txt','a')
    time30.write("2023/12/5 15:36:0" + "\n")
    time30.close
    
    time3 =  open('test1.txt','a')
    time3.write("2023/12/5 15:36:0" + "\n")
    time3.close
    
    return redirect(url_for("LoginScreen"))


@app.route("/NG")
def LoginScreen0():
    
    comment1="そのUserIDとPasswordの組み合わせだと"
    comment2="登録できません"
    
    return render_template("login.html", comment1=comment1, comment2=comment2)






@app.route("/00/<string:int_params>")
def hello_world(int_params):
    data_number = int(int_params)
    
    #f = open('cal.txt','w')
    #f.write(calendar.calendar(2023,c=12,m=1))
    #f.close
    
    #f = open('UserName.txt','w')
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
    
    d13=[]
    d =  open('day.txt','r')
    day = d.readlines()
    d.close
    for i in day:
        istrip=i.strip("\n")
        d13.append(istrip)
    
    
    
    d14=[]
    d =  open('day1.txt','r')
    day1 = d.readlines()
    d.close
    for i in day1:
        istrip=i.strip("\n")
        d14.append(istrip)
    
    
    
    d15=[]
    d =  open('dbid.txt','r')
    dbid = d.readlines()
    d.close
    for i in dbid:
        istrip=i.strip("\n")
        d15.append(istrip)
    
    
    
    kinds=[]
    item=["トレーニング", "食事"]
    d =  open('tra.txt','r')
    tra = d.readlines()
    d.close
    for i in tra:
        istrip=i.strip("\n")
        kinds.append(istrip)
    
    
    currenttime30 =  open('test.txt','r')
    timed30 = currenttime30.readlines()
    currenttime30.close()
    time30_d = timed30[data_number-1]
    ltime30 = time30_d.strip("\n")
    
    
    
    currenttime3 =  open('test1.txt','r')
    timed3 = currenttime3.readlines()
    currenttime3.close()
    time3_d = timed3[data_number-1] 
    ltime3 = time3_d.strip("\n")
    
    
    #x2 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
    d0=d13[data_number-1]
    d01=d14[data_number-1]
    d02=[]
    
    x0 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    z=0
    for i in x0:
        z+=1
        if z == 12:
            break
        if i == d01:
            d =  open('cal'+str(z)+'.txt','r')
            d1 = d.readlines()
            d.close
            d02.append(str(z)+"月")
            day1=str(z)
        
    
    if d01 == "１２月":
        d =  open('cal13.txt','r')
        d1 = d.readlines()
        d.close
        d02.append(str(12)+"月")
        day1=str(12)
    
   
    
    
    x3 = [d1]
    
    x=[]
    data = ToDo.query.all()
    for d in data:
        x.append(d.id)
        
        
        
        

    y=[]
    end_id_number = str(data_number)
    for i in x:
        str_x = str(i)
        str_i = str_x[:-2]
        if str_i.endswith(end_id_number, len(end_id_number)):
            y.append(str(i))
        

    
    
    if len(str(data_number)) == 1:
        acount_dbid = str(0) + str(0) + str(0) + str(data_number)
    if len(str(data_number)) == 2:
        acount_dbid = str(0) + str(0) + str(data_number)
    if len(str(data_number)) == 3:
        acount_dbid = str(0) + str(data_number)
    
    
    
    
        
    if kinds[data_number-1] == "トレーニング":
        z=d15[data_number-1] + str(1)
        x0=[s for s in y if len(s[:-6])==len(str(z)) if str(z) in s]
        if len(x0) == 0:
            z=d15[data_number-1] + str(1) + acount_dbid + str(0) + str(1)
            x0.append(int(z))
        else:
            if len(str(len(x0) + 1)) == 1:
                z=d15[data_number-1] + str(1) + acount_dbid + str(0) + str(len(x0) + 1)
                x0.append(int(z))
    
            else:
                z=d15[data_number-1] + str(1) + acount_dbid + str(len(x0) + 1)
                x0.append(int(z))
                
            
    if kinds[data_number-1] == "食事":
        z=d15[data_number-1] + str(2)
        x0=[s for s in y if len(s[:-6])==len(str(z)) if str(z) in s]
        if len(x0) == 0:
            z=d15[data_number-1] + str(2) + acount_dbid + str(0) + str(1)
            x0.append(int(z))
        else:
            if len(str(len(x0) + 1)) == 1:
                z=d15[data_number-1] + str(2) + acount_dbid + str(0) + str(len(x0) + 1)
                x0.append(int(z))
    
            else:
                z=d15[data_number-1] + str(2) + acount_dbid + str(len(x0) + 1)
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
                x1m=str(max(x1))
                x1mm=int(x1m[-1])
                z=x1m[:-1]+str(x1mm+1)
                x1.append(int(z))
    z0=[int(z)]
    
    reco=[]
    for i in y:
        a=str(i)
        reco.append(a[:-7])
        
    
    recoday=[]
    for i in reco:
        for j in range(1,32):
            if i == str(day1)+str(j):
                recoday.append(j)
    
    setday=set(recoday)
    
    setday_list=list(setday)
    
    setday_str=[]
    #setday_str0=[]
    for i in setday_list:
        a=str(i)
        setday_str.append(a)
        #setday_str0.append(a)
    
    
                
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
        
    for i in range(1,32):
        a=str(i)
        for j in setday_str:
            if a == j:
                x5.pop(i-1)
                x5.insert(i-1,"0")
        
    x2.reverse()
    
    a=["Mo","Tu","We","Th","Fr","Sa","Su"]
    a.append(d02[0])
    
    tore=["トレーニング"]
    
    eat="食事"
    
    kinds0 = kinds[data_number-1]
    
    if eat == kinds[data_number-1]:
        ltime = ltime3
    else:
        ltime = ltime30
    
    
    
    #aaaaa=1271000201
    x4 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    
    return render_template("cal.html", a=a, x3=x3, x4=x4, x5=x5,d0=d0, d01=d01, d15=d15[data_number-1], 
                                      item=item, kinds=[kinds[data_number-1]], kinds0=kinds0, x0=x0, 
                                      tore=tore, eat=eat, x1=x1, x2=x2, y=y, z0=z0, data=data, reco=reco, recoday=recoday, 
                                      setday=setday, setday_list=setday_list, setday_str=setday_str, ltime=ltime,
                                      int_params=int_params)
                                      
    
@app.route("/result0/<string:int_params>", methods=["POST"])
def hello0(int_params):
    data_number=int(int_params)
    
    
    tra_d = request.form["a"]
    tra = open('tra.txt','r')
    tra_r = tra.readlines()
    tra.close
    tra_r[data_number-1]=str(tra_d) + "\n"
    
    
    
    tra = open('tra.txt','w')
    tra.writelines(tra_r)
    tra.close
    
    return redirect(url_for('hello_world', int_params=int_params))


@app.route("/result/<string:int_params>", methods=["POST"])
def hello(int_params):
    data_number=int(int_params)
    
    #day_d = name
    day_d = request.form["a"]
    day = open('day.txt','r')
    day_r = day.readlines()
    day.close
    day_r[data_number-1]=str(day_d) + "\n"
    
    day = open('day.txt','w')
    day.writelines(day_r)
    day.close
    
    
    
    #month_d = name1
    month_d = request.form["b"]
    month = open('day1.txt','r')
    month_r = month.readlines()
    month.close
    month_r[data_number-1]=str(month_d) + "\n"
    
    month = open('day1.txt','w')
    month.writelines(month_r)
    month.close
    
    x1 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    z=0
    a=0
    for i in x1:
        z+=1
        if i == month_d:
            dbid = open("dbid.txt", "r")
            dbid_r = dbid.readlines()
            dbid.close()
            dbid_r[data_number-1]=str(z) + str(day_d) + "\n"
            
            dbid = open("dbid.txt", "w")
            dbid.writelines(dbid_r)
            dbid.close()
    
    
    #x3=[d1]
    return redirect(url_for('hello_world', int_params=int_params))

@app.route("/result1/<string:int_params>", methods=["POST"])
def hell(int_params):
    data_number=int(int_params)
    
    
    
    name = request.form["c"]
    tra =  open('tra.txt','r')
    tra_r = tra.readlines()
    tra.close
    
    kinds = str(tra_r[data_number-1])
    tore = "トレーニング\n"
    return render_template("hozon.html", name=name, kinds=kinds, tore=tore, int_params=int_params)


a=0
@app.route("/result2/<string:int_params>", methods=["POST"])
def hel(int_params):
    data_number=str(int_params)
    name = request.form["a"]
    name1 = request.form["b"]
    name2 = request.form["c"]
    name3 = request.form["d"]
    name4 = request.form["e"]
    name5 = request.form["f"]
    name0 = request.form["g"]
    
    if len(data_number) == 1:
        acount_dbid = str(0) + str(0) + str(0) + data_number
    if len(data_number) == 2:
        acount_dbid = str(0) + str(0) + data_number
    if len(data_number) == 3:
        acount_dbid = str(0) + data_number
    
    str_dbid = str(name0) + str(acount_dbid)
    dbid = int(str_dbid)

    
    new_todo = ToDo(id = name0, starttime=name, site=name1, content=name2, nunber=name3, time=name4, weight=name5)
    db.session.add(new_todo)
    db.session.commit()
    
    
    return redirect(url_for('hello_world', int_params=int_params))
    

@app.route('/del_todo/<string:int_params>/<int:id>')
def del_todo(int_params,id):
	del_data = ToDo.query.filter_by(id=id).first()
	db.session.delete(del_data)
	db.session.commit()
	return redirect(url_for('hello_world', int_params=int_params))
	


@app.route('/date/<string:int_params>', methods=['POST'])
def date(int_params):
    data_number=int(int_params)
    
    name = request.form["a"]
    stime = name.split(":")
    
    dt_now = datetime.datetime.now()#datetime.datetime.now(pytz.timezone('Asia/Tokyo'))#datetime.datetime.now()
    
    year = dt_now.year
    month = dt_now.month
    day = dt_now.day
    
    dt_now0 = datetime.datetime(year, month, day, int(stime[0]), int(stime[1]))
    dt_now1 = dt_now0 + datetime.timedelta(minutes=+30)
    
    year = dt_now1.year
    month = dt_now1.month
    day = dt_now1.day
    hour = dt_now1.hour
    minute = dt_now1.minute
    second = dt_now1.second#dt_now0 = datetime.datetime(year, month, day, hour, stime[0], stime[1])
    
    time = str(year) + "/" + str(month) + "/" +str(day+1) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    name = request.form["a"]
    
    
    time30 = open('test.txt','r')
    time30_r = time30.readlines()
    time30.close
    time30_r[data_number-1]=str(time) + "\n"
    
    time30 =  open('test.txt','w')
    time30.writelines(time30_r)
    time30.close
    
    return redirect(url_for('hello_world', int_params=int_params))



@app.route('/date0/<string:int_params>', methods=['POST'])
def date0(int_params):
    data_number=int(int_params)
    
    name = request.form["a"]
    stime = name.split(":")
    
    dt_now = datetime.datetime.now()#datetime.datetime.now(pytz.timezone('Asia/Tokyo'))#datetime.datetime.now()
    
    year = dt_now.year
    month = dt_now.month
    day = dt_now.day
    
    dt_now0 = datetime.datetime(year, month, day, int(stime[0]), int(stime[1]))
    dt_now1 = dt_now0 + datetime.timedelta(hours=+3)
    
    year = dt_now1.year
    month = dt_now1.month
    day = dt_now1.day
    hour = dt_now1.hour
    minute = dt_now1.minute
    second = dt_now1.second#dt_now0 = datetime.datetime(year, month, day, hour, stime[0], stime[1])
    
    time = str(year) + "/" + str(month) + "/" +str(day+1) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    
    name = request.form["a"]
    
    
    
    time3 = open('test1.txt','r')
    time3_r = time3.readlines()
    time3.close
    time3_r[data_number-1]=str(time) + "\n"
    
    
    time3 =  open('test1.txt','w')
    time3.writelines(time3_r)
    time3.close
    
    return redirect(url_for('hello_world', int_params=int_params))


        

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
    app.debug = True