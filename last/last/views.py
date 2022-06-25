from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Phone
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'layout.html')

def register(request):
    if request.method=='GET':
      return render(request,'register.html')
    elif request.method=='POST':
        username=request.POST['user']
        email=request.POST['email']
        password1=request.POST['pass1']        
        password2=request.POST['pass2'] 
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1,email=email)
            
            print('usercreated')  
            return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
def login1(request):
    if request.method=='GET':
         return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            print('hello',user)
            login(request,user)
            print('success')
            return render(request,'userpage.html')
        else:
            messages.info(request,'invalid credentials' )
            print('failed')
            return redirect('login')
@login_required
def phonenum(request):
    
    if request.method=='GET':
         return render(request,'addphone.html')
    elif request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        Phone.objects.create(uid=request.user,name=name,phone=phone) 
        return render(request,'userpage.html')
def viewphone(request):
    a=Phone.objects.filter(uid=request.user.id)
    context={}
    context['data']=a
    return render(request,'viewphone.html',context)
def logout1(request):
    logout(request)
    return redirect('/')