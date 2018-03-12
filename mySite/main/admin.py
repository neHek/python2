from django.contrib import admin
from main.models import Speakers
from main.models import Section

admin.site.register(Section)

def make_ivan(modeladmin, request, queryset):
    queryset.update(name='Иван Кокарев')


class SpeakerAdmin(admin.ModelAdmin):
    ordering = ['name']
    actions = [make_ivan]
    list_filter=('sect',)
    search_fields = ['name','topic','descr']

admin.site.register(Speakers, SpeakerAdmin)