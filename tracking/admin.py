from django.contrib import admin
from .models import *
# Register your models here.
# from mapwidgets.widgets import GooglePointFieldWidget


# class CityAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": GooglePointFieldWidget}
#     }

admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Product_Cart)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Shop)
admin.site.register(Test)