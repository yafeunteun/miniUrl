# Register your models here.

from django.contrib import admin

from mini_url.models import MiniUrl


class MiniUrlAdmin(admin.ModelAdmin):
   list_display   = ('urlLong', 'code', 'pseudo', 'nbAccess', 'dateCreation')
   search_fields  = ('urlLong',)
   ordering = ('dateCreation',)
   date_hierarchy = 'dateCreation'


admin.site.register(MiniUrl, MiniUrlAdmin)