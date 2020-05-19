from django.contrib import admin
from .models import Flat, Rent


class FlatsAdmin(admin.ModelAdmin):
    list_display = ('flat_code', 'resident_name', 'monthly_rent')


class RentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat','month', 'rent', 'rent_paid', 'elec_bill', 'elec_bill_paid')


admin.site.register(Flat, FlatsAdmin)
admin.site.register(Rent, RentsAdmin)
