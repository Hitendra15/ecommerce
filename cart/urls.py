from django.urls import path
from . import views

urlpatterns = [
    path('add',views.add_to_cart,name="add_cart"),
    path('cart-overview',views.cart_overview,name="cart-overview"),
    path('cart-delete',views.cart_delete,name="cart_delete"),
    path('cart_update',views.cart_update,name="cart_update"),
]

