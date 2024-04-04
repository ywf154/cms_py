from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from users.models import UserProfile
from vehicles.models import VehicleInfo


class VehicleInline(admin.StackedInline):
    model = VehicleInfo



class UserAdmin(admin.ModelAdmin):
    inlines = [VehicleInline]
    list_display = ('username', 'email', 'mobile', 'gender', 'display_actions')
    search_fields = ('username',)
    exclude = ['add_time']

    def display_actions(self, obj):
        edit_url = reverse('admin:users_userProfile_change', args=[obj.pk])
        delete_url = reverse('admin:users_userProfile_delete', args=[obj.pk])

        edit_button = format_html('<a href="{}" class="admin-edit-button">编辑</a>', edit_url)
        delete_button = format_html('<a href="{}" class="admin-delete-button">删除</a>', delete_url)

        return format_html('{}  {}', edit_button, delete_button)

    display_actions.short_description = '操作'


admin.site.register(UserProfile, UserAdmin)



