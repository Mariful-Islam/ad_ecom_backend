from django.urls import path
from .views import *


urlpatterns = [
    path('', router),
    path('products/', product),
    path('total-cart/', total_cart),
    path('cart/<str:username>/', getCart),
    path('cart-summary/<str:username>/', getCartSummary),
    path('item-increase/<int:id>/', addItemQuantity),
    path('item-decrease/<int:id>/', deleteItemQuantity),
    path('cart-delete/<int:id>/', deleteCartItem),
]
