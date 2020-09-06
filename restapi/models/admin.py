from django.contrib import admin
from .models import post, category, imagenes
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombreCategoria',)


class postAdmin(admin.ModelAdmin):
    list_display = ('title',)

class imagenAdmin(admin.ModelAdmin):
    list_display = ('autor',)

admin.site.register(post, postAdmin)
admin.site.register(category, categoriaAdmin)
admin.site.register(imagenes, imagenAdmin)