from django.contrib import admin
from .models import Address,Order,OrderItem
# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','phone','line1','line2','city','state','country']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','total_amount','is_paid','created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','order','quantity']