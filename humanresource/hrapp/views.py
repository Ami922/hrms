from django.shortcuts import render
from django.template import Template, loader
from django.http import HttpResponse
from .models import *

# Create your views here.

def userData(request):
	template = loader.get_template('login.html')
	context={}
	return HttpResponse(template.render(context,request))
	try:
		uname = request.POST.get('username')
		print(uname)
		upassword = request.POST.get('password')
		check_user = Login.objects.filter(username = uname.exists())
		if check_user == False:
			print(False)
			login_obj = Login(username = uname, password = upassword)
			login_obj.save()
			print(login_obj.id)
			return HttpResponse("Registration Done")
	except Exception as e:
		print(str(e))
		return HttpResponse("Failed")
	return HttpResponse("Already exist")

def empReg(request):
	template = loader.get_template('emp_registration.html')
	context = {}
	return HttpResponse(template.render(context, emp_registration.html))
	try:
		firstname = request.POST.get('fname')
		lastname = request.POST.get('lname')
		dob = request.POST.get('select_msg')
		phone_no = request.POST.get('phone')
		address_details = request.POST.get('address')
		gndr = request.POST.get('gender')
		salary_details = request.POST.get('salary')
		h_date = request.POST.get('hire_date')
		return HttpResponse("Registration Done")
	except Exception as e:
		print(str(e))
		return HttpResponse("Failed")
	
