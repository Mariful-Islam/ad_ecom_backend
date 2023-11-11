from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

@api_view(['GET'])
def router(response):
    routes = [
        'api/',
        'api/products'
    ]
    return Response(routes)



@api_view(['GET'])
def product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def total_cart(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCart(request, username):
    user = Account.objects.get(username=username)
    cart = Cart.objects.filter(user=user)

    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCartSummary(request, username):
    user = Account.objects.get(username=username)
    cartSummary = CartSummary.objects.get(user=user)

    serializer = CartSummarySerializer(cartSummary, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def addItemQuantity(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity += 1
    cart.save()
    serializer = CartSummarySerializer(cart, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def deleteItemQuantity(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity -= 1
    cart.save()
    serializer = CartSummarySerializer(cart, many=False)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def deleteCartItem(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    serializer = CartSummarySerializer(cart, many=False)
    return Response(serializer.data)





