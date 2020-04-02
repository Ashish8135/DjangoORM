from django.contrib import admin
from col import models
from django.contrib.admin import ModelAdmin


class NoticeAdmin(ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['subject','msg']
    list_filter = ['cr_date']


# Register your models here.
admin.site.register(models.Notice, NoticeAdmin)
