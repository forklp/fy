from django.contrib import admin
from offline_repair import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Technician)
admin.site.register(models.Computer)