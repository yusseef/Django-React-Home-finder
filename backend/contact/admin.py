from django.contrib import admin
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email']
    list_per_page = 25
# Register your models here.

admin.site.register(Contact, ContactAdmin)