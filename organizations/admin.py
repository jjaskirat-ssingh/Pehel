from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'objective', 'display')
    list_display_links = ('id', 'name')
    #list_filter = ('name',)
    list_editable = ('display',)
    search_fields = ('name', 'description')
    list_per_page = 25

admin.site.register(Organization, OrganizationAdmin)