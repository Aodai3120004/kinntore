from flask import Flask, request, render_template
import os
import calendar

app = Flask(__name__)

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

    d =  open('cal1.txt','r')
    d1 = d.readlines()
    d.close

    d =  open('cal2.txt','r')
    d2 = d.readlines()
    d.close

    d =  open('cal3.txt','r')
    d3 = d.readlines()
    d.close

    d =  open('cal4.txt','r')
    d4 = d.readlines()
    d.close

    d =  open('cal5.txt','r')
    d5 = d.readlines()
    d.close

    d =  open('cal6.txt','r')
    d6 = d.readlines()
    d.close

    d =  open('cal7.txt','r')
    d7 = d.readlines()
    d.close

    d =  open('cal8.txt','r')
    d8 = d.readlines()
    d.close

    d =  open('cal9.txt','r')
    d9 = d.readlines()
    d.close

    d =  open('cal10.txt','r')
    d10 = d.readlines()
    d.close

    d =  open('cal11.txt','r')
    d11 = d.readlines()
    d.close

    d =  open('cal12.txt','r')
    d12 = d.readlines()
    d.close

    #x1 = ["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]
    x2 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]

    return render_template("cal.html", x2=x2 )

    

@app.route("/result", methods=["GET"])
def hello():
    return "jjj"#render_template("app.html", b=b )
        

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 50000)
    app.debug = True