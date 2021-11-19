from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin



class CervisesInline(admin.StackedInline):
    model = models.Cervises
    extra = 1



class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "id"]
    inlines = [CervisesInline]


class CervisesAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", " procedure_time", "post"]

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Cervises)




# Register your models here.
