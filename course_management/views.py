from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import MySQLdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect

from forms import LoginForm, i_reg, s_reg, c_reg, reg, attend, grades, fb

# Create your views here.

from django.http import HttpResponse
#the views.py file contains functions to be called in events such as form submission

#user.save()

def index(request):
    	if request.method == 'POST':
		# A POST request: Handle Form Upload
		form = LoginForm(request.POST) # Bind data from request.POST into a PostForm
	 	context = { "form":form}
		# If data is valid, proceeds to create a new post and redirect the user
		if form.is_valid():
		   auth = form.cleaned_data['authorization']
		   username = form.cleaned_data['username']
		   password = form.cleaned_data['password']
		   user = authenticate(username = username, password = password)
		   print username
		   print password
		   print auth
		   
		   if user is not None:
			c = connection.cursor()
	 	   	c.execute("select * from %s where username = '%s'" % (auth, username)) 
		   	row = c.fetchone()
			if row is not None:
				login(request, user)
				if auth == 'admin':
					context = {}
					return render(request, "admin_home.html",context)
				if auth == 'instructor':
					c = connection.cursor()
	 	   			c.execute("select * from %s where username = '%s'" % (auth, username)) 
		   			row = c.fetchone()
					c = connection.cursor()
	 	   			c.execute("select * from courses where instructor = %s"%(request.user.username)) 
		   			row2 = c.fetchall()
					row1 = ('course_id','department','name','instructor','credits')
					row2 = (row1,) + row2 
					context = {"name" : row[1],"table":row2}
					return render(request, "instructor_home.html",context)
				if auth == 'student':
					c = connection.cursor()
	 	   			c.execute("select * from %s where username = '%s'" % (auth, username)) 
		   			row = c.fetchone()
					context = {"name" : row[1]}
					return render(request, "student_home.html",context)
			else :
				return HttpResponse("Invalid Authorization")
		   else:
			context = {}
			return render(request, "login_error.html",context)


		   
		   

		'''try:
	 		c = connection.cursor()
	 		c.execute("select * from dept_phone")
	 		row = c.fetchone()
	 		print row
	 	
	 	except Exception,e:
	 		print repr((e[1]))
	 	finally:
	 		c.close()
	 	
	 	db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
	 	c = db.cursor()
	 	#c.execute("select * from STUDENTS")
	 	sql = " INSERT INTO dept_phone VALUES ('%d','%s')" % (101, '1111111111')
	 	c.execute(sql)
	 	db.commit()
	 	#row = c.fetchall()
	 	#print(row)
		   
		'''
	    	return render(request, "login.html",context)
	else:
		form = LoginForm()
		context = { "form":form}
		return render(request, "login.html",context)
def instructor_reg(request):
	#context = RequestContext(request)
	if request.method == 'POST':
		form = i_reg(request.POST)
		context = { "form":form}
		if form.is_valid():
			id = form.cleaned_data['id']
			name = form.cleaned_data['name']
			dept = form.cleaned_data['dept']
			desgn = form.cleaned_data['desgn']
			exp = form.cleaned_data['exp']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username,'', password)
			user = authenticate(username=username)
			print id
			db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
 			c = db.cursor()
 			#c.execute("select * from STUDENTS")
		 	sql = " INSERT INTO instructor VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (id, name, dept, desgn, exp, 				username, password)
			try:
				c.execute(sql)
				db.commit()
				return HttpResponse("Registration Successful")
			except Exception,e: 
				print repr((e[1]))
				return HttpResponse("Registration Unsccessful")
		 	
		 	
		 	#row = c.fetchall()
		 	#print(row)
	else:
		form = i_reg()
		context = {"form":form}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "instructor_reg.html",context)
		

def student_reg(request):
	#context = RequestContext(request)
	if request.method == 'POST':
		form = s_reg(request.POST)
		context = { "form":form}
		if form.is_valid():
			rollno = form.cleaned_data['rollno']
			name = form.cleaned_data['name']
			dept = form.cleaned_data['dept']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username,'', password)
			user = authenticate(username=username)
			print id
			db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
 			c = db.cursor()
 			#c.execute("select * from STUDENTS")
		 	sql = " INSERT INTO student VALUES ('%s','%s','%s','%s','%s')" % (rollno, name, dept, username, password)
			try:
				c.execute(sql)
				db.commit()
				return HttpResponse("Registration Successful")
			except Exception,e: 
				print repr((e[1]))
				return HttpResponse("Registration Unsccessful")
			
				
	else:
		form = s_reg()
		context = {"form":form}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "student_reg.html",context)

def course_reg(request):
	if request.method == 'POST':
		form = c_reg(request.POST)
		context = { "form":form}
		if form.is_valid():
			courseid = form.cleaned_data['courseid']
			name = form.cleaned_data['name']
			dept = form.cleaned_data['dept']
			instructor = form.cleaned_data['instructor']
			credits = form.cleaned_data['credits']
			#user = authenticate(username=username)
			print id
			db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
 			c = db.cursor()
 			#c.execute("select * from STUDENTS")
		 	sql = " INSERT INTO courses VALUES ('%s','%s','%s','%s','%s')" % (courseid, dept, name, instructor, credits)
			try:
				c.execute(sql)
				db.commit()
				return HttpResponse("Registration Successful")
			except Exception,e: 
				print repr((e[1]))
				return HttpResponse("Registration Unsccessful")
			
				
	else:
		form = c_reg()
		context = {"form":form}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "course_reg.html",context)
		

def log_out(request):
	
	context = {}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		logout(request)
		return render(request, "logged_out.html",context)
		
def registration(request):	
		c = connection.cursor()
 	   	c.execute("select * from courses") 
           	row = c.fetchall()
		row1 = ('course_id','department','name','instructor','credits')
		row = (row1,) + row
		if request.method == 'POST':
			form = reg(request.POST)
			context = { "form":form, "table":row}
			if form.is_valid():
				courseid = form.cleaned_data['courseid'] 
				print courseid
				db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
	 			c = db.cursor()
	 			#c.execute("select * from STUDENTS")
			 	sql = "insert into registered values(%s,'%s', '', '', '', '')"%(request.user.username,courseid)
			
				try:
					c.execute(sql)
					db.commit()
					return HttpResponse("Registration Successful")				
				except Exception,e: 
					print repr((e[1]))
					return HttpResponse("Registration Unsccessful")
		else:
			form = reg()
			context = {"form":form, "table":row}
		if not request.user.is_authenticated:
			return HttpResponse("Access Denied")
		else:
			return render(request, "registration.html",context)

def attendance(request):
	c = connection.cursor()
 	c.execute("select courses.course_id,name,rollno,attendance from courses join registered on courses.course_id = registered.course_id where instructor = %s"%(request.user.username)) 
        row = c.fetchall()
	row1 = ('course_id','name','rollno','attendance')
	row = (row1,) + row
	if request.method == 'POST':
		form = attend(request.POST)
		context = {"form" : form, "table" : row}
		if form.is_valid():
			courseid = form.cleaned_data['courseid']
			attendance = form.cleaned_data['attendance']
			rollno = form.cleaned_data['rollno']
			db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
	 		c = db.cursor()
	 		#c.execute("select * from STUDENTS")
			z = connection.cursor()
			z.execute("select * from courses where course_id = '%s' and instructor = '%s'"%(courseid, request.user.username))
			check = z.fetchone()
			if check is None:
				return HttpResponse("Please select a course instructed by you") 
			sql = "update registered set attendance = %s where course_id = '%s' and rollno = %s"%(attendance, courseid, rollno)
			
			try:
				c.execute(sql)
				db.commit()
				return HttpResponse("Attendance update successful")				
			except Exception,e: 
				print repr((e[1]))
				return HttpResponse("Attendance update unsccessful")
	else:
			form = attend()
			context = {"form":form, "table":row}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "attendance.html",context)

def grade(request):
	c = connection.cursor()
 	c.execute("select courses.course_id,name,rollno,grades from courses join registered on courses.course_id = registered.course_id where instructor = %s"%(request.user.username)) 
        row = c.fetchall()
	row1 = ('course_id','name','rollno','grades')
	row = (row1,) + row
	if request.method == 'POST':
		form = grades(request.POST)
		context = {"form" : form, "table" : row}
		if form.is_valid():
			courseid = form.cleaned_data['courseid']
			grade = form.cleaned_data['grade']
			rollno = form.cleaned_data['rollno']
			db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
	 		c = db.cursor()
	 		#c.execute("select * from STUDENTS")
			z = connection.cursor()
			z.execute("select * from courses where course_id = '%s' and instructor = '%s'"%(courseid, request.user.username))
			check = z.fetchone()
			if check is None:
				return HttpResponse("Please select a course instructed by you") 
			sql = "update registered set grades = '%s' where course_id = '%s' and rollno = %s"%(grade, courseid, rollno)
			
			try:
				c.execute(sql)
				db.commit()
				#return HttpResponse("Attendance update successful")
				return render(request, "grade.html",context)				
			except Exception,e: 
				print repr((e[1]))
				return HttpResponse("Attendance update unsccessful")
	else:
			form = grades()
			context = {"form":form, "table":row}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "grade.html",context)

def feedback(request):
	c = connection.cursor()
 	c.execute("select courses.course_id,name,instr_feedback,course_feedback from courses join registered on courses.course_id = registered.course_id where rollno = %s"%(request.user.username)) 
        row = c.fetchall()
	row1 = ('course_id','name','instr_feedback','course_feedback')
	row = (row1,) + row
	if request.method == 'POST':
		form = fb(request.POST)
		context = {"form" : form, "table" : row}
		if form.is_valid():
			courseid = form.cleaned_data['courseid']
			c_feedback = form.cleaned_data['course_feedback']
			i_feedback = form.cleaned_data['i_feedback']
			db = MySQLdb.connect("localhost","divyanshkc","dishuiit","course_management")
	 		c = db.cursor()
	 		#c.execute("select * from STUDENTS")
			z = connection.cursor()
			z.execute("select * from registered where course_id = '%s' and rollno = '%s'"%(courseid, request.user.username))
			check = z.fetchone()
			if check is None:
				return HttpResponse("Please select a course taken by you") 
			sql = "update registered set course_feedback = '%s' where course_id = '%s' and rollno = %s"%(c_feedback, courseid, request.user.username)
			sql2 = "update registered set instr_feedback = '%s' where course_id = '%s' and rollno = %s"%(i_feedback, courseid, request.user.username)
			try:
				c.execute(sql)
				c.execute(sql2)
				db.commit()
				return HttpResponse("Feedback Recorded. Thank You!")
				#return render(request, "grade.html",context)				
			except Exception,e: 
				print repr((e[1]))
				return HttpResponse("There was an error in recieving feedback.")
	else:
			form = fb()
			context = {"form":form, "table":row}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "feedback.html",context)

def stud_display(request):
	c = connection.cursor()
	c.execute("select courses.course_id,name,department,credits,attendance,grades from courses join registered on courses.course_id = registered.course_id where rollno = %s"%(request.user.username))
	row = c.fetchall()
	row1 = ('course_id','name', 'department','credits','attendance','grades')
	row = (row1,) + row
	context = {"table" : row}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "student_display.html",context)

				
def view_fb(request):
	c = connection.cursor()
	c.execute("select courses.course_id,instr_feedback,count(instr_feedback) from courses join registered on courses.course_id = registered.course_id where instructor = '%s' group by courses.course_id,instr_feedback"%(request.user.username))
	row = c.fetchall()
	print row
	row1 = ('course_id','feedback','count')
	row = (row1,) + row
	print row
	d = connection.cursor()
	d.execute("select courses.course_id,course_feedback,count(course_feedback) from courses join registered on courses.course_id = registered.course_id where instructor = '%s' group by courses.course_id,course_feedback"%(request.user.username))
	row2 = d.fetchall()
	row1 = ('course_id','feedback','count')
	row2 = (row1,) + row2
	context = {"table" : row,"table2" : row2}
	if not request.user.is_authenticated:
		return HttpResponse("Access Denied")
	else:
		return render(request, "view_feedback.html",context)

def home(request):
	c = connection.cursor()
 	c.execute("select * from student")
 	row = c.fetchall()
 	context = {"table":row}
	return render(request, "home.html",context)
