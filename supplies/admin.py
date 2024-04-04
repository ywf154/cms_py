from django.contrib import admin

from supplies.models import *


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = ['add_time']


class Supplies_categoryAdmin(admin.ModelAdmin):
    list_display = ['supplier','name','brand']
    exclude = ['add_time']


class SuppliesInfoAdmin(admin.ModelAdmin):
    list_display = ['category','name','price','number']
    exclude = ['add_time']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Supplies_category, Supplies_categoryAdmin)
admin.site.register(SuppliesInfo, SuppliesInfoAdmin)
