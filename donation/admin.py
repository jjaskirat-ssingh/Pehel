from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email')
  list_display_links = ('id', 'name')
  #list_filter = ('pickup_date',)
  search_fields = ('name', 'email')#, 'pickup_date')
  list_per_page = 25

admin.site.register(Donation, DonationAdmin)