from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from .models import Category,Anime


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


class register_user(View):
    def get(self,request):
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Succesufully Registered Created"))
            return redirect('home')
        else:
            messages.success(request, (form.errors))
            return redirect('register')
    
# def register_user(request):
# 	form = SignUpForm()
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password1']
# 			# log in user
# 			user = authenticate(username=username, password=password)
# 			login(request, user)
# 			messages.success(request, ("Username Created"))
# 			return redirect('home')
# 		else:
            
# 			messages.success(request, (form.errors))
# 			return redirect('register')
# 	else:
# 		return render(request, 'register.html', {'form':form})

def product(request,pk):
    product = Product.objects.get(id=pk)
    
    return render(request,'product.html',{'product':product})

def category(request,foo):
    #Grab catagory
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.error(request,("That category does not exists"))
        return redirect('home')
    
    
def anime_based(request,foo):
    
    
    if foo=='all':
        anime=list(Anime.objects.exclude(name="NONE"))
        return render(request,'anime.html',{'animes':anime})
    else:
        #Grab catagory
        try:
            anime=Anime.objects.get(name=foo)
            products=Product.objects.filter(anime=anime)
            return render(request,'anime_based.html',{'products':products,'anime':anime})
        except:
            messages.error(request,("That anime does not exists"))
            return redirect('home')
        
class UserPage(View):
    def get(self,request:HttpRequest):
         
        
        return render(request,'userpage.html',{})
    
