import mysql.connector as a
mydb=a.connect(
	host='localhost',
	user='root',
	password='Password',
	database='class')
def monitor():
	o=int(input("1. Update Monitor  2. Check Monitor\n"))
	if o==1:
		r=input("Enter Student Roll no.: ")
		n=input("Enter Student's Name: ")
		c=input("Enter Month: ")
		cmd="insert into monitor values(%s,%s,%s)"
		data=(r,n,c)
		cur=mydb.cursor()
		cur.execute(cmd,data)
		mydb.commit()
		print("Data Entered Sucessfully!")
		main()
	else:
		s="select * from monitor"
		cur=mydb.cursor()
		cur.execute(s)
		d=cur.fetchall()
		for i in d:
			print(i)
		main()
def marks():
	o=int(input("1. Update Marks 2. Check Marks\n"))
	if o==1:
		r=input("Enter Student Roll: ")
		n=input("Enter Student Name: ")
		s1=float(input("Subject 1: "))
		s2=float(input("Subject 2: "))
		s3=float(input("Subject 3: "))
		t=s1+s2+s3;
		per=(t/300)*100;
		term=input("Enter Term: ")
		data=(r,n,s1,s2,s3,t,per,term)
		sql="insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s)"
		cur=mydb.cursor()
		cur.execute(sql,data)
		mydb.commit()
		print("Data Entered Sucessfully!!!")
		main()
	else:
		r=input("Enter Roll : ")
		t=input("Enter Term : ")
		sql="select * from marks where roll=%s and term= %s"
		cur=mydb.cursor()
		cur.execute(sql,(r,t))
		for i in cur:
			print(i)
		main()
def att():
	o=int(input("1. Update Attendence 2.Check Attendence \n"))
	if o==1:
		d=input("Enter Date: ")
		ab=input("Enter Roll Numbers: ")
		data=(d,ab)
		sql="insert into att values(%s,%s)"
		cur=mydb.cursor()
		cur.execute(sql,data)
		mydb.commit()
		print("Data Entered Sucessfully")
		main()
	else:
		sql="select * from att"
		cur=mydb.cursor()
		cur.execute(sql)
		d=c.fetchall()
		for i in d:
			print(i)
		main()
def student():
	o=int(input("1. Update Atttendence  2. Check Attendence \n"))
	if o==1:
		r=input("Enter Student Roll: ")
		n=input("Enter Student Name: ")
		p=input("Enter Phone: ")
		a=input("Enter Address: ")
		data=(r,n,p,a)
		sql="insert into students values(%s,%s,%s,%s)"
		cur=mydb.cursor()
		cur.execute(sql,data)
		mydb.commit()
		print("Data Entered Sucessfully!!")
		main()
	else:
		sql="select * from students"
		cur=mydb.cursor()
		cur.execute(sql)
		d=c.fetchall()
		for i in d:
			print(i)
		main()
def main():
	print('''
		1.Monitor
		2.Report Card
		3.Attendence
		4.Students
		''')
	choice=input("Enter Task No: ")
	while True:
		if(choice=='1'):
			monitor()
		elif (choice=='2'):
			marks()
		elif (choice=='3'):
			att()
		elif (choice=='4'):
			student()
		else:
			print("Wrong Choice.....")
			break;
print('''
  ,ad8888ba,  88                 db        ad88888ba   ad88888ba   
 d8"'    `"8b 88                d88b      d8"     "8b d8"     "8b  
d8'           88               d8'`8b     Y8,         Y8,          
88            88              d8'  `8b    `Y8aaaaa,   `Y8aaaaa,    
88            88             d8YaaaaY8b     `"""""8b,   `"""""8b,  
Y8,           88            d8""""""""8b          `8b         `8b  
 Y8a.    .a8P 88           d8'        `8b Y8a     a8P Y8a     a8P  
  `"Y8888Y"'  88888888888 d8'          `8b "Y88888P"   "Y88888P"   ''')
main()


