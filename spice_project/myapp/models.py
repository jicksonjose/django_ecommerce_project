from django.db import models

# Create your models here.

class user_details(models.Model):
    fname= models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pin = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.fname


class contact_support(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     phone = models.IntegerField()
     message =models.CharField(max_length=100)

     def __str__(self):
         return self.name

class category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class item(models.Model):
    item_name = models.CharField(max_length=100)
    original_rate = models.FloatField()
    item_rate = models.FloatField()
    item_pic = models.ImageField()
    item_description = models.CharField(max_length=100)
    opng_stock = models.IntegerField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)


    def __str__(self):
        return self.item_name


class review(models.Model):
    item_name = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=50)
    rate = models.IntegerField(default=0, null=True)
    date=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.item_name


class wishlist(models.Model):
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    category_name = models.ForeignKey(category, on_delete=models.CASCADE)
    rate = models.IntegerField()
    item_pic = models.CharField(max_length=100)


class wishlist_products(models.Model):
    item = models.ForeignKey(item, on_delete=models.SET_NULL, null=True)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()



class cart(models.Model):
    customer = models.ForeignKey(user_details, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)

class CartProduct(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "cart:" + str(self.cart.id) + "cartproduct:" + str(self.id)

class Order_address(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(user_details, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    pin = models.IntegerField()
    state = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    def __str__(self):
        return "order:" + str(self.id)



ORDER_STATUS = (
    ("order processing", "order processing"),
    ("order confirmed", "order confirmed"),
    ("order on the way", "order on the way"),
    ("order received", "order received"),
    ("order cancelled", "order cancelled")
)


class Orders(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(user_details, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    pin = models.IntegerField()
    state = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    cancel_request = models.CharField(max_length=100, default='none')

    def __str__(self):
        return "order:" + str(self.id)


