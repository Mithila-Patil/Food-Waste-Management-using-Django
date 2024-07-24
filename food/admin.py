from django.contrib import admin
from .models import Donor, Receiver, FoodDonor

admin.site.register(Donor)
admin.site.register(Receiver)

class FoodDonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'address', 'food_info', 'quantity', 'pick_up_date')
    search_fields = ('name', 'city', 'phone')
    list_filter = ('city', 'pick_up_date')

admin.site.register(FoodDonor, FoodDonorAdmin)