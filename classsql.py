import mysql.connector
mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='Password'
	)
cur=mydb.cursor()
s1="create database class"
cur.execute(s1)
s2="use class"
cur.execute(s2)
s3="create table monitor(roll varchar(5) primary key,name varchar(5),month varchar(15))"
cur.execute(s3)
s4="create table marks(roll varchar(5) primary key,name varchar(20),s1 int,s2 int,s3 int,total int,per float,term varchar(20))"
cur.execute(s4)
s5="create table att(date varchar(10),abs varchar(500))"
cur.execute(s5)
s6="create table students(roll varchar(5),name varchar(50),phone varchar(15),address varchar(50))"
cur.execute(s6)
mydb.commit()