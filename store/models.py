from django.db import models
import datetime

# Categories of Products
class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Mets:
        verbose_name_plural = 'categories'



class Anime(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    first_name=models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=8)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    anime=models.ForeignKey(Anime,on_delete=models.CASCADE,blank=True,null=True)
    # Add Sale Stuff
    
    is_sale= models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=8)
    
    
    def __str__(self):
        return f"{self.name}"
    
    
# Customer Orders

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=20)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.product


class Size(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    sizes = models.CharField(max_length=2, choices=SIZE_CHOICES)
    count=models.IntegerField(default=0)
    
    def __str__(self):
        return self.sizes
    
    
