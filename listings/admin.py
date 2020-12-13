from django.contrib import admin
from .models import Listing
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display=['id','title','is_published','price','list_date','realtor']
    list_display_links=['id','title']
    list_filter=('realtor','garage','bedrooms','bathrooms')
    list_editable=('is_published',)
    search_fields=('title','price','state','city','address','zipcode')
    list_per_page=25
# admin.site.register(Listing,ListingAdmin)

