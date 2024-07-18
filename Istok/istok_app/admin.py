from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Определяет количество пустых форм для загрузки дополнительных изображений

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'sale_price', 'description')
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)

admin.site.register(UserProfile)
admin.site.register(RenovationLocation)
admin.site.register(Order)
admin.site.register(Favorite)
admin.site.register(BonusProgram)
admin.site.register(Category)
