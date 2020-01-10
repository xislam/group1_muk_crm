from django.contrib import admin
from accounts.models import User, Profile, Passport, AdminPosition, UserAdminPosition, Role, UserRole, SocialStatus
from django.contrib.auth.admin import UserAdmin


# class ProfileInline(admin.StackedInline):
#     model = Profile
#     exclude = ['user']
#
#
# class ProfileAdmin(UserAdmin):
#     inlines = [ProfileInline]
#

# admin.site.unregister(User)
# admin.site.register(User, ProfileAdmin)

# admin.site.register(Profile)
admin.site.register(Passport)
admin.site.register(AdminPosition)
admin.site.register(UserAdminPosition)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(SocialStatus)
