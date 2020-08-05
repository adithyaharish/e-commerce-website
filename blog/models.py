from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from phone_field import PhoneField
# Create your models here.
#from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),
    ('CA','Casuals'),
    ('AC','Accessories')

)



class contact_details(models.Model):
   name = models.CharField(max_length=100, blank=True, null=True)
   subject = models.CharField(max_length=120)
   email = models.EmailField(max_length = 254)
   message = models.TextField(blank=True)
   
   def __str__(self):
       return self.name
       
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })
        

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    #start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.CharField(max_length=100)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', on_delete=models.SET_NULL, blank=True, null=True)
    street_address = models.CharField(max_length=120,blank=True, null=True)
    phone=PhoneField(blank=True)
    appartment_address = models.CharField(max_length=120,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    zip = models.CharField(max_length=100,blank=True, null=True)
   
    
    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    phone=PhoneField(blank=True)
    appartment_address = models.CharField(max_length=100)
    state = models.CharField(max_length=100,blank=True)
    zip = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username

    
    
    