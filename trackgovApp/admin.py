from django.contrib import admin
from .models import UserRegistration, HouseOfRepsBills, HrepsPoliticiansInfo, HrepsVotePatterns


# Modyfying the HouseOfRepsBills model to be more efficient in the admin panel aqnd to have better display
class HouseOfRepsBillsAdmin(admin.ModelAdmin):
    list_display = ('title_of_bill', 'date', 'category', 'chamber', 'status', 'stage_of_bill', 'portfolio', 'summary', 'link_to_bill')
    search_fields = ['title_of_bill', 'summary']

class HrepsPoliticiansInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'elec_div', 'position', 'party', 'phone_number', 'email_address', 'twitter', 'facebook', 'bio_link', 'profile_picture')
    search_fields = ['party', 'elec_div']


class HrepsVotePatternsAdmin(admin.ModelAdmin):
    list_display = ('title', 'div_no', 'question', 'date', 'outcome', 'politician_name', 'party', 'ayes_vote', 'noes_vote')
    search_fields = ['title', 'politician_name', 'party']



# One way to register models(Tweaking the display)
admin.site.register(HouseOfRepsBills, HouseOfRepsBillsAdmin)
admin.site.register(HrepsPoliticiansInfo, HrepsPoliticiansInfoAdmin)
admin.site.register(HrepsVotePatterns, HrepsVotePatternsAdmin)


# Alternative way to register models
admin.site.register(UserRegistration)


