from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Change avatar", {
            "fields": ['avatar']
        }),
    )


admin.site.register(CustomUser, CustomAdmin)
