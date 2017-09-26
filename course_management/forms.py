from django import forms

class LoginForm(forms.Form):
    	CHOICES = [('admin','admin'),('instructor','instructor'),('student','student')]
    	authorization = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
    	username = forms.CharField(max_length=256)
    	password = forms.CharField(min_length = 5, max_length=30, widget=forms.PasswordInput())

class i_reg(forms.Form):
	id = forms.CharField(max_length=11)
	name = forms.CharField(max_length=30)
	dept = forms.CharField(max_length=11)
	desgn = forms.CharField(max_length=30)
	exp = forms.IntegerField(max_value = 99, min_value=0)
	username = forms.CharField(max_length=30)
	password = forms.CharField(min_length = 5, max_length=30, widget=forms.PasswordInput())

class s_reg(forms.Form):
	rollno = forms.CharField(max_length=11)
	name = forms.CharField(max_length=30)
	dept = forms.CharField(max_length=11)
	username = forms.CharField(max_length=30)
	password = forms.CharField(min_length = 5, max_length=30, widget=forms.PasswordInput())

class c_reg(forms.Form):
	courseid = forms.CharField(max_length=30)
	dept = forms.CharField(max_length=30)
	name = forms.CharField(max_length=30)
	instructor = forms.CharField(max_length=30)
	credits = forms.IntegerField(max_value=99, min_value=0)

class reg(forms.Form):
	courseid = forms.CharField(max_length=30)

class attend(forms.Form):
	courseid = forms.CharField(max_length=30)
	rollno = forms.CharField(max_length = 11)
	attendance = forms.IntegerField(max_value = 99, min_value = 0)
	
class grades(forms.Form):
	courseid = forms.CharField(max_length=30)
	rollno = forms.CharField(max_length = 11)
	grade = forms.CharField(max_length=2)

class fb(forms.Form):
	courseid = forms.CharField(max_length = 30)
	CHOICES = [('Good','Good'),('Average','Average'),('Poor','Poor')]
	course_feedback=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
	i_feedback = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())

		
	
