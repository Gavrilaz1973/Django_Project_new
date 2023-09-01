from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)


# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_staff = request.user.is_staff
#
#         if is_staff:
#             form.product_fields['name'].disabled = True
#         return form