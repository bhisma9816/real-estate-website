from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','listings','contact_date')
    list_display_links =('id','name')
    search_fields = ('email','name','listings')
    list_per_page = 25
# Register your models here.
admin.site.register(Contact , ContactAdmin)
