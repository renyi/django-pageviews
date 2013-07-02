from django.contrib import admin
from .models import HitCount


class HitCountAdmin(admin.ModelAdmin):
	list_display = ('url', 'hits')


admin.site.register(HitCount, HitCountAdmin)
