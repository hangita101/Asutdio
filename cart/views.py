from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.views import View
from django.http import HttpRequest
# Create your views here.

def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods()
    return render(request,"cart_summary.html",{"cart_products":cart_products})



class cart_add(View):
    def post(self,request:HttpRequest):
        cart=Cart(request)
        product_id= int(request.POST.get('product_id'))
            
            # lookup
        product=get_object_or_404(Product,id=product_id)
            
        cart.add(product=product)            

        cart_quantity=cart.__len__()
        
        
        return JsonResponse({'productName':product.name,'qty':cart_quantity})
                

def cart_delete(request):
    return render(request,"cart_summary.html",{})
def cart_update(request):
    return render(request,"cart_summary.html",{})
