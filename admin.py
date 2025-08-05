from django.contrib import admin
from .models import Store, Category, MenuItem, Order, OrderItem

#blog/admin.py

admin.site.register(Store)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

