from django.contrib import admin

from .models import Birthday

admin.site.empty_value_display = 'Не задано'

class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday'
    )
    list_editable = (
        'first_name',
        'last_name',
        'birthday'
    )
    search_fields = ('last_name',)
    list_display_links = ('id',)

admin.site.register(Birthday, BirthdayAdmin)