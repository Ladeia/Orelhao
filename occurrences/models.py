from django.db import models

class OccurrenceType(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True)
