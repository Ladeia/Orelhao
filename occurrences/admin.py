from django.contrib import admin
from .models import OccurrenceType

admin.site.register(OccurrenceType)

class OccurrenceTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
