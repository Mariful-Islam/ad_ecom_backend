from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist


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
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def total_cart(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCart(request, username):

    try:
        user = Account.objects.get(username=username)
        if not user:
            pass
        else:
            cart = Cart.objects.filter(user=user)
            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)

    except:
        pass
    
    return Response()

       
    


@api_view(['GET'])
def getCartItem(request, username, id):
    user = Account.objects.get(username=username)
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(user = user, product = product)

    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def addToCart(request, username, id):
    user = Account.objects.get(username=username)
    product = Product.objects.get(id=id)
    print(product.name)
    try:
        cart = Cart.objects.get(user=user, product=product)
        print(cart)
        if cart:
            cart.quantity+=1
            cart.save()
        else:
            new_cart = Cart.objects.create(user=user,
                                    product=product,
                                    quantity=1)
            new_cart.save()
            
    except:
        new_cart = Cart.objects.create(user=user,
                                    product=product,
                                    quantity=1)
        new_cart.save()
    
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def addItemQuantity(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity += 1
    cart.save()
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def deleteItemQuantity(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity -= 1
    cart.save()
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def deleteCartItem(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == "POST":
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        user = None
        if not user:
            user = authenticate(username=username, password=password)
            print(user)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': username,'token': token.key}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response()



@api_view(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)

        user = None
        if not user:
            user = authenticate(username=username, password=password)
            print(user)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': username,'token': token.key}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid Credintial'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response()
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == "POST":
        try:
            request.user.authtoken_token.delete()
            return Response({'message': 'Successfully Log Out'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'erroe': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





