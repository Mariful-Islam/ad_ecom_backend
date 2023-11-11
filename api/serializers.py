from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id',
                  'user', 
                  'product', 
                  'quantity', 
                  'product_name', 
                  'product_image', 
                  'product_price',]
        

class CartSummarySerializer(ModelSerializer):
    class Meta:
        model = CartSummary
        fields = ['cart_total_number', 'cart_total_price']

