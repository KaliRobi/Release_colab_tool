from django.contrib import admin
from defects.models import Comment, Defect
# Register your models here.

class DefectsAdming(admin.ModelAdmin):
    list_display = ['defect_number']

admin.site.register(Comment)
admin.site.register(Defect, DefectsAdming)