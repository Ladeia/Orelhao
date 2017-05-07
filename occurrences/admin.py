from django.contrib import admin
from .models import OccurrenceType

class OccurrenceTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def __unicode__(self):
        return self.title; 

admin.site.register(OccurrenceTypeAdmin)
