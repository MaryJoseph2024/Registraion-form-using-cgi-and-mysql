#!C:\Users\JOSE\AppData\Local\Programs\Python\Python38\python.exe
import pymysql
import cgi,cgitb
print("Content-type:text/html")
print()
form=cgi.FieldStorage()
fullname=form['username'].value
emailID=form['email'].value
pwd=form['password'].value
address=form['textcontent'].value
gender=form['sex'].value
phno=form['phno'].value
hobby=form['hobbies'].value
db=pymysql.connect(host="localhost",user="root",password="")
cursor=db.cursor()
#print("connected")
cursor.execute("Drop database if exists MaryNew")
cursor.execute("Create database MaryNew")
cursor.execute("Use MaryNew")
#print("inside Mary")
cursor.execute("Drop table if exists registration")
#print("Table dropped")
cursor.execute("Create table registration (Name char(20) primary key,emailID varchar(25),password varchar(20), Address varchar(20),gender char(15),phonenum bigint,hobbies varchar(20))")
val=fullname,emailID,pwd,address,gender,phno,hobby
#print("Table created")
sql="Insert into registration(Name,emailID,password,Address,gender,phonenum,hobbies) values(%s,%s,%s,%s,%s,%s,%s)"
try:
    
    cursor.execute(sql,val)
    print("Saved successfully")
   
except:
    db.rollback()

db.commit()
db.close()
print("<html>")
print("<head>")
print("<title> CGI Registration Form with Database connectivity </title>")
print("</head>")
print("<body>")
print("<h2> Hello!%s </h2>" %(fullname))
print("Database created successfully <br/>")
print("Table created successfully<br/>")
print("Saved successfully <br/>")
print("</body>")
print("</html>")



