from django.shortcuts import render
from django.template import Template, loader
from django.http import HttpResponse
from . models import *

# Create your views here.

# def userData(request):
# 	template = loader.get_template('login.html')
# 	context={}
# 	return HttpResponse(template.render(context,request))
# 	try:
# 		uname = request.POST.get('username')
# 		print(uname)
# 		upassword = request.POST.get('password')
# 		check_user = Login.objects.filter(username = uname.exists())
# 		if check_user == False:
# 			print(False)
# 			login_obj = Login(username = uname, password = upassword)
# 			login_obj.save()
# 			print(login_obj.id)
# 			return HttpResponse("Registration Done")
# 	except Exception as e:
# 		print(str(e))
# 		return HttpResponse("Failed")
# 	return HttpResponse("Already exist")

# def empReg(request):
# 	template = loader.get_template('emp_registration.html')
# 	context = {}
# 	return HttpResponse(template.render(context, emp_registration.html))
# 	try:
# 		firstname = request.POST.get('fname')
# 		lastname = request.POST.get('lname')
# 		dob = request.POST.get('select_msg')
# 		phone_no = request.POST.get('phone')
# 		address_details = request.POST.get('address')
# 		gndr = request.POST.get('gender')
# 		salary_details = request.POST.get('salary')
# 		h_date = request.POST.get('hire_date')
# 		return HttpResponse("Registration Done")
# 	except Exception as e:
# 		print(str(e))
# 		return HttpResponse("Failed")
	
# def upLoad(request):
# 	template = loader.get_template('image.html')
# 	context = {}
# 	if request.method =='POST' and request.FILES['file_upload']:
# 			print("upload Post")
# 			myfile = request.FILES['file_upload']
# 			print(myfile)
# 			# fname = request.POST.get('names')
# 			# print(fname)
# 			objUpload = Upload( image=myfile)
# 			objUpload.save()
# 			print(objUpload)
# 			context['Msg'] = 'File Upload Successfully'
# 			context['img'] = objUpload.image
# 	return HttpResponse(template.render(context, request))

def projectReg(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			title = request.POST.get('ptitle')
			sponser = request.POST.get('psponser')
			cost = request.POST.get('pcost')
			manager = request.POST.get('pmanger')
			sdate = request.POST.get('psdate')
			edate = request.POST.get('pedate')
			reg_obj = ProjectRegister(project_title=title, project_sponser=sponser, project_manager=manager, 
				      project_cost=cost, project_start_date=sdate, project_end_date=edate )
			reg_obj.save()
			return HttpResponse("Registration Done")
			return render(request,'project_manager_home.html')

		except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'project_register.html')

def complaintReg(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			ename = request.POST.get('name')
			eid = request.POST.get('id')
			edesg = request.POST.get('post')
			edept = request.POST.get('dept')
			eaddress = request.POST.get('addr')
			ephone = request.POST.get('phone')
			cname = request.POST.get('compname')
			cdesg = request.POST.get('cpost')
			cdept = request.POST.get('cdept')
			cact =request.POST.get('act')
			date = request.POST.get('date')
			time = request.POST.get('time')
			comp_reg = ComplaintReg(e_name=ename, e_desgination=edesg, e_dept=edept, e_addr=eaddress,
			           e_phone=ephone, c_name=cname, complaint_desg=cdesg, complaint_dept=cdept,
			           compaint_description=cact, date_of_incident=date, time_of_incident=time)
			comp_reg.save()
			return HttpResponse("Registration Done")
			return render(request,'employee_home.html')

		except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'emp_complaint_form.html')


def performanceEvaluation(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			ename = request.POST.get('name')
		except Exception as a:
			print(str(a))
			return HttpResponse("Failed")
	return render(request, 'emp_complaint_form.html')


