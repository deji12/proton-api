from django.contrib import admin
from .models import Note, Profile, User, GeneratePassword, DeveloperMode

# Register your models here.
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Profile)
admin.site.register(GeneratePassword)
admin.site.register(DeveloperMode)