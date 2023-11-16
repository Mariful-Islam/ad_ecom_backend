from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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
        


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"



class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account(
            username = validated_data['username'],
            email = validated_data['email']
            )
        user.set_password(raw_password=validated_data['password'])
        user.save()
        
        return user