from django.contrib import admin
from .models import Client, Organization, Bills

admin.site.register(Client)
admin.site.register(Organization)
admin.site.register(Bills)
