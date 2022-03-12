from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'organization', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  list_filter = ('organization',)
  search_fields = ('name', 'email', 'organization')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)