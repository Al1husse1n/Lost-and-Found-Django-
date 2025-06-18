from django.contrib import admin
from .models import UserProfile, LostItem
admin.site.register(LostItem)
admin.site.register(UserProfile)
# Register your models here.
