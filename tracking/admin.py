from django.contrib import admin
from .models import *
# Register your models here.
# from mapwidgets.widgets import GooglePointFieldWidget


# class CityAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": GooglePointFieldWidget}
#     }

admin.site.register(Order)
admin.site.register(Driver)
admin.site.register(Shop)