from django.contrib import admin
from .models import *


admin.site.site_header="Auto Parts Finder"
# Register your models here.

admin.site.register(Part_category)
admin.site.register(Part_manufacture)
admin.site.register(Make)
admin.site.register(Manufacture)

admin.site.register(Body_type)
admin.site.register(Supplier)
admin.site.register(Service)
admin.site.register(Specialist)
admin.site.register(Part_name)
@admin.register(Equery)
class Enqueries(admin.ModelAdmin):
    list_display=['part_name','car_model','name','last_name','phone']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','date']
@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ['name','date','ip_address']

admin.site.register(Part)


