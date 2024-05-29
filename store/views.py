from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    products = Product.objects.all()
    
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html',{})



class login_user(View):
    def get(self,request:HttpRequest):
        return render(request,'login.html',{})
        
    def post(self,request:HttpRequest):
        username=request.POST['username']
        password=request.POST['password']
                    
        
        user=authenticate(request,username=username,password=password)
        
        
        if user is not None:
            login(request,user)
            messages.success(request,("Successifully Logged In"))
            return redirect('home')
        else:
            
            messages.error(request,("There was an error during logging in "))
            return redirect('login')
    
def logout_user(request):
    logout(request)
    messages.success(request,("Logged Out"))
    return redirect('home')