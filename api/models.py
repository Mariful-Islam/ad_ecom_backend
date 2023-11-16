from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username
    

class Product(models.Model):
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
    
