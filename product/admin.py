from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from product.models import CustomUser, Product

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_no', 'profile_pic')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ['email', 'first_name', 'phone_no', 'profile_pic']
    search_fields = ['first_name', 'email']
    ordering = ['first_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']
    search_fields = ['name']
    ordering = ['name']




