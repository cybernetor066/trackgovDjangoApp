from django.contrib import admin
from .models import UserRegistration, HouseOfRepsBills


# Modyfying the HouseOfRepsBills model to be more efficient in the admin panel aqnd to have better display
class HouseOfRepsBillsAdmin(admin.ModelAdmin):
    list_display = ('title_of_bill', 'date', 'category', 'chamber', 'status', 'stage_of_bill', 'portfolio', 'summary', 'link_to_bill')
    search_fields = ['title_of_bill', 'summary']

admin.site.register(HouseOfRepsBills, HouseOfRepsBillsAdmin)









# Register your models here.
admin.site.register(UserRegistration)

# admin.site.register(HouseOfRepsBills)


