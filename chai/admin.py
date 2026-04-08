from django.contrib import admin
from .models import ChaiVariety,ChaiReveiw,Store,ChaiCertificate
# Register your models here.
class ChaiReveiwInline(admin.TabularInline):
    model=ChaiReveiw
    extra=2
class ChaivarietyAdmin(admin.ModelAdmin):
    list_display=['name','type','date_added']
    inlines=[ChaiReveiwInline]
class StoreAdmin(admin.ModelAdmin):
    list_display=['name','location']
    filter_horizontal=['chai_varieties']
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=['chai','certificate_number','issue_date','valid_untill']
admin.site.register(ChaiVariety,ChaivarietyAdmin)
#admin.site.register(ChaiReveiw)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
