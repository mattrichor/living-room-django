from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Person, Memory, SocialPost
admin.site.register(Person)
admin.site.register(Memory)
admin.site.register(SocialPost)
