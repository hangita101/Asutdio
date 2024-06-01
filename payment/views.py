from django.shortcuts import render,redirect
from django.views import View
from cart.cart import Cart
from django.http import HttpRequest,Http404
from django.contrib.auth.models import User
from django.contrib import messages 
# Create your views here.

class Checkout(View):
    def get(self,request):
        cart=Cart(request)
        cart_products=cart.get_prods()
        quantities =cart.get_qunats()
        grandtotal=cart.cart_total()        
        return render(request,'checkout.html',{'cart_products':cart_products,'quantities':quantities,'totals':grandtotal})


class Method(View):
    def get(self,request:HttpRequest):  
        messages.error(request,"no")
        return Http404()
        
    def post(self,request):
        pmethod= request.POST.get('pmethod')
        print(pmethod)    
        if not request.user.is_authenticated:
            messages.error(request,"Please Log in")    
            return redirect('login')
        if pmethod=="Esewa" :
            return render(request,"esewa.html",{})
        elif pmethod=="Khalti":
            return render(request,"khalti.html",{})
        