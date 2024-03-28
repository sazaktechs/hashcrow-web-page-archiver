''' The Django admin site '''
from django.contrib import admin
from .models import Hash

admin.site.register(Hash)
