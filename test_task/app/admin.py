from django.contrib import admin

from .models import Program, Category, Product



class ProgramAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Program._meta.fields]
admin.site.register(Program, ProgramAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Category._meta.fields]
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Product._meta.fields]
admin.site.register(Product, ProductAdmin)
