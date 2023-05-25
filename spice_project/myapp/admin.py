from django.contrib import admin
from . models import *

class itemAdmin(admin.ModelAdmin):
    list_display = ('item_name',  'original_rate','item_rate', 'item_pic', 'opng_stock', 'category')

    def item_pic(self, obj):
        return '<img src="%s" width="50" height="50" />' % obj.image.url

    item_pic.allow_tags = True
    item_pic.short_description = 'Image'



class user_detailsAdmin(admin.ModelAdmin):
    list_display = ('fname','lname', 'address', 'phone','state','pin', 'email')


#
class cartAdmin(admin.ModelAdmin):
    list_display = ( 'customer', 'total')

class cart_productsAdmin(admin.ModelAdmin):
    list_display = ( 'cart', 'item', 'rate' ,'quantity', 'subtotal')

# class whislistAdmin(admin.ModelAdmin):
#     list_display = ( 'user', 'item')
class orderAdmin(admin.ModelAdmin):
    list_display = (  'customer', 'total', 'order_status', 'created_at', 'address', 'mobile'  ,'pin', 'state', 'cancel_request')


# Register your models here.

admin.site.register(item, itemAdmin)
admin.site.register(user_details, user_detailsAdmin)
admin.site.register(category)

# admin.site.register(wishlist, whislistAdmin)
# admin.site.register(wishlist_products)
admin.site.register(cart,  cartAdmin)
admin.site.register(CartProduct, cart_productsAdmin)
admin.site.register(Orders, orderAdmin)
# admin.site.register(review)
# admin.site.register(payment_details)
admin.site.register(contact_support)
admin.site.register(Order_address)
