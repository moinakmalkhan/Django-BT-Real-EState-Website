from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts
def register(request):
    if request.method=='POST':
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check password
        if password != password2:
            messages.error(request,"Password do not match")
            return redirect("register")
        # check username
        if User.objects.filter(username=username).exists():
            messages.error(request,"This Username is already takem")
            return redirect("register")
        # check email
        if User.objects.filter(email=email).exists():
            messages.error(request,"This email is being used")
            return redirect("register")
        # When every thing is ok
        user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()
        messages.success(request,"You are now registered and can log in.")
        return redirect("login")
    else:
        return render(request,"accounts/register.html")
def login(request):
    if request.method=='POST':
        # Login User
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are loged in")
            return redirect('dashboard')
        else:
            messages.error(request,"Username or password is incorrect.")
            return redirect("login")

    else:
        return render(request,"accounts/login.html")
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,"You are now loged out")
        return redirect("home")
def dashboard(request):
    cont=Contacts.objects.all().order_by("-contact_date").filter(user_id=request.user.id)
    context={'cont':cont}
    return render(request,"accounts/dashboard.html",context)
