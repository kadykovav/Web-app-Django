from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, RoleUser, Teacher


admin.site.register(User, UserAdmin)
admin.site.register(RoleUser)
admin.site.register(Teacher)




