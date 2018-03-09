from django.contrib import admin
from main.models import Speakers
from main.models import Section

admin.site.register(Section)

def make_ivan(modeladmin, request, queryset):
    queryset.update(name='Иван')


class SpeakerAdmin(admin.ModelAdmin):
    ordering = ['name']
    actions = [make_ivan]

admin.site.register(Speakers, SpeakerAdmin)