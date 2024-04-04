from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from vehicles.models import *


class BrandInfoAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    exclude = ['add_time']


class Product_Year_MonthAdmin(admin.ModelAdmin):
    fields = ['year', 'month']


class VariantInfoAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', ]
    exclude = ['add_time']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['image_display', 'name', 'variant', 'user', ]  # 'display_actions'
    exclude = ['add_time']

    def image_display(self, obj):
        return format_html('<img src="{}" width="100" height="60" alt="Image">', obj.image.url)

    image_display.short_description = '车辆照片'

    # def display_actions(self, obj):
    #     edit_url = reverse('admin:vehicles_vehicleInfo_change', args=[obj.pk])
    #     delete_url = reverse('admin:vehicles_vehicleInfo_delete', args=[obj.pk])
    #
    #     edit_button = format_html('<a href="{}" class="admin-edit-button">编辑</a>', edit_url)
    #     delete_button = format_html('<a href="{}" class="admin-delete-button">删除</a>', delete_url)
    #
    #     return format_html('{}  {}', edit_button, delete_button)
    #
    # display_actions.short_description = '操作'


admin.site.register(VehicleInfo, VehicleAdmin)
admin.site.register(BrandInfo, BrandInfoAdmin)
admin.site.register(Product_Year_Month, Product_Year_MonthAdmin)
admin.site.register(VariantInfo, VariantInfoAdmin)
