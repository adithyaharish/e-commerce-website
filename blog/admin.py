from django.contrib import admin
from .models import contact_details,Item,OrderItem,Order,Address

class OrderAdmin(admin.ModelAdmin):
    list_display=['user','ordered','shipping_address']
    
    list_display_links = [
        'shipping_address','user']
    
    list_filter = ['ordered','delivered']
    search_fields = ['user', 'ordered']

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'appartment_address',
        'state',
        'zip',
        'phone'
    ]
    list_filter = ['street_address', 'zip','user']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

class OrderItemAdmin(admin.ModelAdmin):
     list_display=['item','ordered']
     list_filter = ['ordered']

admin.site.register(contact_details)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Item)
admin.site.register(Address, AddressAdmin)