from django.urls import path
from .views import *


urlpatterns = [
    path('', router),
    path('products/', products),
    path('product/<int:id>/', getProduct),
    path('total-cart/', total_cart),
    path('cart/<str:username>/', getCart),
    path('cart-item/<int:id>/', getCartItem),
    path('add-cart/<str:username>/<int:id>/', addToCart),
    path('item-increase/<int:id>/', addItemQuantity),
    path('item-decrease/<int:id>/', deleteItemQuantity),
    path('cart-delete/<int:id>/', deleteCartItem),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
