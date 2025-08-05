from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="category_icons/")
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    min_order_price = models.IntegerField()
    delivery_fee = models.IntegerField()
    image = models.ImageField(upload_to="store_images/")
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="menu_images/")
    def __str__(self):
        return self.name

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through="OrderItem")
    address = models.CharField(max_length=200)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.items

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.order
