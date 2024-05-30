from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    return render(request,"cart_summary.html",{})




def cart_add(request):
    #get cart
    cart=Cart(request)
    
    if request.POST.get('action')=='post':
        #Get Stuffs
        product_id=int(request.POST.get('product_id'))
        #lookup product in DB
        product = get_object_or_404(Product,id=product_id)
        
        cart.add(product=product)
        
        response = JsonResponse({'Product Name' : product.name})
        return response
        

def cart_delete(request):
    return render(request,"cart_summary.html",{})
def cart_update(request):
    return render(request,"cart_summary.html",{})
