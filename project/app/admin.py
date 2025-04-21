from django.contrib import admin
from  .models import Bd
from  .models import Rubric


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price')
    list_display_links = ('title',)
    search_fields = ('title', )
class RubAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Rubric, RubAdmin)
admin.site.register(Bd, BdAdmin)