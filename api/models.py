from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username
    

class Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField()
    desc = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.product.name
    
    def username(self):
        return self.user.username
    
    def product_name(self):
        return self.product.name
    
    def product_image(self):
        return self.product.image.url
    
    def product_price(self):
        return self.product.price
    
    # def cart_total_number(self):
    #     quantity = 0
    #     for cart in Cart.objects.all():
    #         quantity += cart.quantity
        
    #     return quantity


    # def cart_total_price(self):
    #     price = 0
    #     for cart in Cart.objects.all():
    #         price += cart.product.price
        
    #     return price

class CartSummary(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.cart.user.username
    
    def cart_total_number(self):
        quantity = 0
        for cart in CartSummary.objects.all():
            quantity += cart.cart.quantity
        
        return quantity

    def cart_total_price(self):
        price = 0
        for cart in CartSummary.objects.all():
            price += cart.cart.product.price*cart.cart.quantity
        
        return price