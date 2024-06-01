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
    quantities =cart.get_qunats()
    return render(request,"cart_summary.html",{"cart_products":cart_products,'quantities':quantities})



class cart_add(View):
    def post(self,request:HttpRequest):
        cart=Cart(request)
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
        product = get_object_or_404(Product, id=product_id)
		
		# Save to session
        cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
        cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response            
                

def cart_delete(request):
    return render(request,"cart_summary.html",{})
def cart_update(request):
    return render(request,"cart_summary.html",{})
