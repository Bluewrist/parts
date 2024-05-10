from django.db import models
from django.urls import reverse
from PIL import Image,ImageDraw,ImageFont
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.contrib.auth.models import User

import uuid


class Customer(User):
    phone = models.CharField(max_length=20,null=True)
    phone2 = models.CharField(max_length=20,null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    suplies = models.CharField(max_length=200,default='')
    date_registered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    service = models.CharField(max_length=200)
    provider = models.ForeignKey(Supplier,on_delete=models.CASCADE)

    def __str__(self):
        return self.service
    
class Specialist(models.Model):
    special = models.CharField(max_length=200)
    provider = models.ForeignKey(Supplier,on_delete=models.CASCADE)

    def __str__(self):
        return self.service

class Search(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(default='',max_length=200)
    users = models.CharField(default='',max_length=200)

    def __str__(self):
        return self.name

    

    def __str__(self):
        return self.name

class Manufacture(models.Model):
    name = models.CharField(max_length=200)
    decs = models.TextField(blank=True,null=True)
    logo = models.ImageField(default='default.jpg',upload_to='cars')
    country = models.CharField(default='',max_length=200)
    def __str__(self):
        return self.name


class Body_type(models.Model):
    name = models.CharField(max_length=200)
    decs = models.TextField(blank=True,null=True)
    

    def __str__(self):
        return self.name
  

class Make(models.Model):
    name = models.CharField(max_length=200)
    manufacture = models.ForeignKey(Manufacture,on_delete=models.CASCADE)
    body_type = models.ForeignKey(Body_type,on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg',upload_to='cars')
    model_number = models.CharField(default='',max_length=200)
    decs = models.TextField(blank=True,null=True)

    def __str__(self):
        return "%s %s   %s" %(self.year,self.manufacture.name,self.name)


class Part_category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    name = models.CharField(max_length=200)
    decs = models.TextField(blank=True,null=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=False, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])  

    
    


class Part_manufacture(models.Model):
    name = models.CharField(max_length=200)
    decs = models.TextField(blank=True,null=True)
    logo = models.ImageField(default='default.jpg',upload_to='cars')

    def __str__(self):
        return self.name
class Part_name(models.Model):
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Part_category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Equery(models.Model):
    part_name = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)




class Part(models.Model):
    part_name = models.ForeignKey(Part_name,on_delete=models.CASCADE,blank=True,null=True)
    part_number_1 = models.CharField(max_length=200,unique=True)
    part_number_2 = models.CharField(max_length=200,unique=True,blank=True,null=True)
    part_number_3 = models.CharField(max_length=200,unique=True,blank=True,null=True)
    manufacture = models.ForeignKey(Part_manufacture,on_delete=models.CASCADE,blank=True,null=True)
    car_model = models.ForeignKey(Make,on_delete=models.CASCADE,related_name='car_models')
    image = models.ImageField(default='default.jpg',upload_to='cars')
    des = models.TextField()
    price = models.IntegerField()
    suppliers = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    compatable_models = models.ManyToManyField(Make,related_name="bidders",blank=True)
    trending = models.BooleanField(default=False)
    just_arrived = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    slug = models.SlugField(default='',max_length=200,editable=False)



    def __str__(self):
        return "%s %s   %s  %s" %(self.car_model.year,self.car_model.manufacture.name,self.car_model.name,self.part_name.name)
    
    def get_absolute_url(self):
        kwargs = {
            'pk':self.pk,
            'slug':self.slug
        }
        return reverse("part-detail", kwargs=kwargs)
    
    def save(self,*args,**kwargs):
        value =  "%s %s   %s  %s" %(self.car_model.year,self.car_model.manufacture.name,self.car_model.name,self.part_name.name)
        self.slug = slugify(value,allow_unicode=True)
        super().save(*args,**kwargs)
    
class Watchlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Part,on_delete=models.SET_NULL,blank=True,null=True)


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date_orderd =  models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) 
    transaction_id =  models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return str(self.transaction_id)
    

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


    @property
    def get_vat(self):
        total = self.get_cart_total
        vat = 15/100 * total
        return vat
    
    @property
    def grand_total(self):
        total = self.get_cart_total + self.get_vat
        return total

    @property
    def address(self):
        address = self.diliveryAddress_set.all()
        return address
    

class OrderItem(models.Model):
    product = models.ForeignKey(Part, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL,blank=True,null=True )
    quantity = models.IntegerField(default=0)
    date_orderd =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.part_name 

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class DiliveryAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    first_name =  models.CharField(max_length=200,null=True,blank=True)
    last_name =  models.CharField(max_length=200,null=True,blank=True)
    phone =  models.CharField(max_length=200,null=True,blank=True)
    phone2 =  models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    suburb =  models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=20,default='123 angwa harare')
    date_orderd =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

