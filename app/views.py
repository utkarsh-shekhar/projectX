from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.models import User
from .models import Expense
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def IndexView(request):
	if request.method=="GET":
		return render(request, 'app/index.html', { })
	elif request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		# for user in User.objects.all:
		# 	print(user, user.get_username())
		print('---------------')
		try:
			if username != None and password != None:
				user = authenticate(username=username, password=password)
				LoginStatus = False
				print("HEHHEHHEHEHE")
				if user is not None:
					print(LoginStatus, request.user.username)
					login(request, user)
					LoginStatus = True
					return render(request,"app/index.html",{'LoginStatus':LoginStatus,'first_name':request.POST.get('first_name',""),'last_name':request.POST.get('last_name',"")})
				else:
					print(LoginStatus)
					return render(request,"app/index.html",{'LoginStatus':LoginStatus})
			else:
				print("username or password is null")
		except Exception as e:
			print("EXCCET", e)
	else:
		print("Other request than get or post ")


def CreateUser(request):
	if request.method=="GET":
		return render(request,'app/signup.html',{})
	elif request.method=="POST":
		print("Here")
		username=request.POST['username']
		password=request.POST['password']
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		email=request.POST['email']
		if username and password and firstname and email:
			try:
				user=User.objects.create_user(username,email,password)
				user.first_name=firstname
				user.last_name=lastname
				user.save()
				print('success')
			except:
				print("Username already exists")
		else:
			print("username or password or firstname or email is blank")
		return render(request,"app/index.html",{})
	else:
		print("username or password is null")


def Transactions(request):
	e = Expense(Transaction_No = 1,
		PaidBy = 'aaaaaaa',
		Amount = 2,
		OwnedBy = 'a',
		Description = 'asd')
	e.save()
	transactions_list = Expense.objects.all()

	context = {
		'transactions_list': transactions_list,
	}
	#return HttpResponse(request, 'app/All_Transactions.html', context)
	return render(request, 'app/All_Transaction.html', context)

def My_transactions(request):
    transactions_list = Expense.objects.filter(Q(PaidBy=request.user.username) |
                               Q(OwnedBy=request.user.username)).order_by('-DateTime')[:-5]
    context = {
        'transactions_list': transactions_list,
    }
    return HttpResponse(request, 'app/My_ransactions.html', context)
# def login(request):
# 	return render(request, 'app/index.html', { })
