from django.contrib import admin
from munros.models import Munro

class MunroAdmin(admin.ModelAdmin):
    pass
admin.site.register(Munro, MunroAdmin)
