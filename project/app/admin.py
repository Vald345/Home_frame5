from django.contrib import admin
from  .models import Bd


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price')
    list_display_links = ('title',)
    search_fields = ('title', )

admin.site.register(Bd, BdAdmin)