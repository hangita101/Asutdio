from django.urls import path
from . import views

urlpatterns = [
    path('checkout',views.Checkout.as_view(),name="checkout"),
    path('checkout/method',views.Method.as_view(),name="paymethod"),

]
