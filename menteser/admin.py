from django.contrib import admin
from .models import Transtorno
from users.models import User, Profile

admin.site.register(Transtorno)
admin.site.register(User)
admin.site.register(Profile)