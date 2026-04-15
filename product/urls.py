from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name="product"),
    path('<slug:slug>',views.product_detail,name="detail")
]
