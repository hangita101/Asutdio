from django.contrib import admin
from .models import Category,Customer,Order,Product,Size
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Size)
