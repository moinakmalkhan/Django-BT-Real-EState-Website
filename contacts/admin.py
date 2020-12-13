from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display=['id','name','listing','email','phone','contact_date']
    list_display_links=['id','name']
    search_fields=('name','email','listing')
    list_per_page=25
admin.site.register(Contacts, ContactsAdmin)
