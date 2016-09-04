from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.
def IndexView(request):
	if request.method=="GET":
		return render(request, 'app/index.html', { })
	elif request.method=="POST":
		username=request.POST.get('username',"")
		password=request.POST.get('password',"")
		if username!=null and password!=nulll:
			user=authenticate(username=username,password=password)
			LoginStatus=False
			if user is not None:
				authenticate.login(request.user)
				LoginStatus=True
				return render(request,"app/index.html",{'LoginStatus':LoginStatus,'first_name':request.POST.get('first_name',""),'last_name':request.POST.get('last_name',"")})
			else:
				return render(request,"app/index.html",{'LoginStatus':LoginStatus})
		else:
			print("username or password is null")
	else:
		print("Other request than get or post ")
		
		
def CreateUser(request):
	if request.method=="GET":
		return render(request,'app/createuser.html',{})
	elif request.method=="POST":
		username=request.POST.get('username',"")
		password=request.POST.get('password',"")
		firstname=request.POST.get('first_name',"")
		lastname=request.POST.get('last_name',"")
		email=request.POST.get('email',"")
		if username and password and firstname and email:
			try:
				user=User.objects.create_user(username,email,password)
				user.first_name=firstname
				user.last_name=lastname
				user.save()
			except:
				print("Username already exists")
		else:
			print("username or password or firstname or email is blank")
		return render(request,"index.html",{})
	else:
			print("username or password is null")
			
	
			
def login(request):
	return render(request, 'app/index.html', { })
