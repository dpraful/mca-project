from django.contrib import admin

from HelathApp import models

# Register your models here.
admin.site.register(models.reg)
admin.site.register(models.Hospital)
admin.site.register(models.FieldWorker)
admin.site.register(models.HealthAlert)
admin.site.register(models.Mobile_Healthcare_Unit)
admin.site.register(models.DiseaseCaseReport)
admin.site.register(models.Disease)
admin.site.register(models.Region)
admin.site.register(models.DiseasePrediction)
# admin.site.register(models.Campaign)
admin.site.register(models.CampCompletionReport)
admin.site.register(models.Survey)
