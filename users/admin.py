from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'phoneNumber']
    list_display = ('full_name', 'phoneNumber', 'staff', 'admin')

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
