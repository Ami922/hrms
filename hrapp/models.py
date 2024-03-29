from django.db import models

class Ip(models.Model):


class Attendance(models.Model):
	date = models.DateField(max_length=25)
	time = models.DateField(max_length=25)
	fk_ip_id = models.ForeignKey(Ip, on_delete=models.CASCADE)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class Complaint(models.Model):
	e_name = models.CharField(max_length=25)
	e_desgination = models.CharField(max_length=25)
	e_dept = models.CharField(max_length=25)
	e_addr = models.CharField(max_length=25)
	e_phone = models.IntegerField()
	c_name = models.CharField(max_length=25)
	complaint_desg = models.CharField(max_length=25)
	complaint_dept = models.CharField(max_length=25)
	compaint_description = models.CharField(max_length=60)
	date_of_incident = models.DateField(max_length=25)
	time_of_incident = models.DateField(max_length=25)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class PerformanceEvaluation(models.Model):
	emp_name = models.CharField(max_length=25)
	emp_dept = models.CharField(max_length=25)
	date = models.DateField(max_length=25)
	project = models.CharField(max_length=25)
	emp_duty = models.CharField(max_length=100)
	emp_strength = models.CharField(max_length=75)
	emp_weakness = models.CharField(max_length=75)
	plan_to_improve = models.CharField(max_length=75)
	fk_project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class Intimation(models.Model):
	emp_name = models.CharField(max_length=25) 
	date = models.DateField(max_length=25)
	mail = models.CharField(max_length=25)
	dept = models.CharField(max_length=25)
	reason = models.CharField(max_length=50)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class EmployeeLeave(models.Model):
	emp_name = models.CharField(max_length=50)
	dept = models.CharField(max_length=50)
	leave_available = models.IntegerField()
	leave_taken = models.IntegerField()
	leave_remains = models.IntegerField()
	leave_type = models.CharField(max_length=50)
	from_date = models.DateField(max_length=50)
	to_date = models.DateField(max_length=50)
	no_of_days = models.IntegerField()
	leave_reason = models.CharField(max_length=50)
 	
class Project(models.Model):
	project_title = models.CharField(max_length=50)
	project_sponser = models.CharField(max_length=50)
	project_manger = models.CharField(max_length=25)
	project_cost = models.IntegerField()
	project_start_date = models.DateField(max_length=25)
	project_end_date = models.DateField(max_length=25)
	project_expense = models.IntegerField(max_length=25)


class Resource(models.Model):
	hardware_req = models.CharField(max_length=50)
	software_req = models.CharField(max_length=50)
	equipment_req = models.CharField(max_length=50)


class ResourceAllocate(models.Model):
	project_title = models.CharField(max_length=25)
	dept = models.CharField(max_length=25)
	task_title = models.CharField(max_length=25)
	resource_type = models.CharField(max_length=25)
	resource_available = models.CharField(max_length=25)
	resource_allocated = models.CharField(max_length=25)
	fk_resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
	fk_project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
	

class CompanyProfile(models.Model):
	company_title = models.CharField(max_length=20)
	company_estb_year = models.IntegerField()
	address = models.CharField(max_length=100)
	phone = models.IntegerField()
	fax = models.IntegerField()
	website = models.CharField(max_length=25)
	email = models.CharField(max_length=25)	


class TaskAdd(models.Model):
    fk_project_id  = models.IntegerField(ProjectRegister, max_length=25)
    task_title = models.CharField(max_length=50)
    task_priority = models.CharField(max_length=25)
    task_start_date = models.DateField(max_length=25)
    task_end_date = models.DateField(max_length=25)
    team_lead = models.CharField(max_length=50)
	
class TaskAssign(models.Model):
	team_lead = models.CharField(max_length=25)
	fk_employee_id = models.IntegerField(Employeeprofile, max_length=25)
	fk_task_id = models.IntegerField(TaskAdd, max_length=25)
	reminder = models.DateField(max_length=25)

class CostEstimation(models.Model):
	software_cost = models.IntegerField()
	hardware_cost = models.IntegerField()
	equipment_cost = models.IntegerField()
	total_cost = models.IntegerField()


class Intimation(models.Model):
	mail = models.CharField(max_length=50)
	intimation_date = models.DateField(max_length=25)
	intimation_description = models.CharField(max_length=60)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class Vacany(models.Model):
	no_of_vacanies = models.IntegerField(max_length=25)
	dept_name = models.CharField(max_length=25)
	post = models.CharField(max_length=25)
	emp_qualification = models.CharField(max_length=25)
	emp_experience = models.CharField(max_length=25)
	time_period = models.DateField(max_length=25)


class Permission(models.Model):
	fk_role_id = models.ForeignKey(Company, on_delete=models.CASCADE)
	permission_title = models.CharField(max_length=20)


class Login(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	fk_role = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)


class Role(models.Model):
	role_title = models.CharField(max_length=15)
	fk_company_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)


class Resume(models.Model):
	resume= models.FileField(upload_to ='file/')
	fk_candidate = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)


class CandidateExperiance(models.Model):
	company_name = models.CharField(max_length=20)
	designation = models.CharField(max_length=15)
	period = models.IntegerField()
	fk_candidate = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)


class Interview(models.Model):
	interview_type = models.CharField(max_length=20)
	interview_Date = models.DateField()
	interview_time = models.IntegerField()
	interview_location = models.CharField(max_length=20)
	fk_candidate = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)


class CallLetter(models.Model):
	fk_candidate = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)
	fk_interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
	post = models.CharField(max_length=20)
	join_date = models.DateField()
	join_time = models.CharField(max_length=10)


class QuestionPaper(models.Model):
	question = models.CharField(max_length=50)
	answer = models.CharField(max_length=20)


class MockTest(models.Model):
	mock_question = models.CharField(max_length=50)
	mock_answer = models.CharField(max_length=20)


class ExamDetail(models.Model):
	exam_startdate = models.DateField()
	exam_enddate = models.DateField()
	exam_time = models.CharField(max_length=10)
	exam_duration = models.CharField(max_length=10)


class Mail(models.Model):
	from_address = models.CharField(max_length=20)
	to_address = models.CharField(max_length=20)
	content = models.CharField(max_length=100)
	attachment = models.FileField(upload_to ='')



class Result(models.Model):
	fk_candidate = models.ForeignKey(CandidateRegistration, on_delete=models.CASCADE)
	mark = models.IntegerField()
	rank = models.CharField(max_length=10)

	
class User(models.Model):
	upload_image= models.FileField(upload_to ='pictures/')
	fname = models.CharField(max_length=25)
	lname = models.CharField(max_length=25)
	gender = models.CharField(max_length=25)
	dob = models.DateField(max_length=25)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	password = models.CharField(max_length=15)
	designation = models.CharField(max_length=15)
	emp_qualification = models.CharField(max_length=25)
	emp_experience = models.CharField(max_length=25)
	salary = models.CharField(max_length=25)
	join_date = models.CharField(max_length=25)







	