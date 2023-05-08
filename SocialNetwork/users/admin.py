from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'last_login', 'last_request')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email', 'last_login', 'last_request')
    list_filter = ('last_login', 'last_request')
    search_fields = ('first_name', 'last_name', 'username', 'email')


admin.site.register(User, UserAdmin)
