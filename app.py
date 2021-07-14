from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/search')
def search():
   return render_template('search.html')
@app.route('/update')
def updatemain():
   return render_template('update.html')
@app.route('/updatesal')
def updatemainsal():
   return render_template('updatesal.html')

@app.route('/delete')
def deletemain():
   return render_template('delete.html')

@app.route('/newrecord')
def newrecord():
   return render_template('newrecord.html')

@app.route('/range')
def range():
   return render_template('range.html')

@app.route('/addpic')
def addpic():
   return render_template('addpic.html')

@app.route('/namesearch', methods=['POST','GET'])
def list():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    field=request.form['name']
    print(field)
    querry="Select * from people WHERE Name =  '"+field+"' "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/all', methods=['POST','GET'])
def fulllist():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    querry="Select * from people "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/keyupdate',methods=['POST','GET'])
def update():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['keyword'])
        querry="UPDATE people SET keywords = '"+keyword+"'   WHERE Name ='"+name+"' "
        cur.execute(querry)
        conn.commit()
        querry2="Select * from people "
        cur.execute(querry2)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

@app.route('/addpicture',methods=['POST','GET'])
def addpicture():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        pic= str(request.form['pic'])
        querry="UPDATE people SET Picture = '"+pic+"'   WHERE Name ='"+name+"' "
        cur.execute(querry)
        conn.commit()
        querry2="Select * from people "
        cur.execute(querry2)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

@app.route('/salaryupdate',methods=['POST','GET'])
def chnagesal():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['sal'])
        querry="UPDATE people SET salary = '"+keyword+"'   WHERE Name ='"+name+"' "
        cur.execute(querry)
        conn.commit()
        querry2="Select * from people "
        cur.execute(querry2)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

@app.route('/namedelete', methods=['GET', 'POST'])
def deleterecord():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        querry="DELETE FROM people WHERE Name ='"+name+"' "
        cur.execute(querry)
        conn.commit()
        querry2="Select * from people "
        cur.execute(querry2)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

@app.route('/sal', methods=['GET', 'POST'])
def notmatch():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        maxsal= str(request.form['maxsal'])
        minsal= str(request.form['minsal'])
        querry="select * from people WHERE Salary  BETWEEN '"+minsal+"' AND '"+maxsal+"' "
        cur.execute(querry)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

@app.route('/addperson', methods=['GET', 'POST'])
def addperson():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        state= str(request.form['state'])
        sal= str(request.form['sal'])
        grade= str(request.form['grade'])
        room= str(request.form['room'])
        num= str(request.form['num'])
        pic= str(request.form['pic'])
        key= str(request.form['key'])
        querry="INSERT INTO people VALUES ('"+name+"','"+state+"','"+sal+"','"+grade+"','"+room+"','"+num+"','"+pic+"','"+key+"')"
        cur.execute(querry)
        conn.commit()
        querry1="select * from people "
        cur.execute(querry1)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.debug=True
    app.run()
    