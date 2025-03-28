from django.contrib import admin
from .models import Comment, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image') 
    search_fields = ('name',)  
    list_filter = ('price',)

admin.site.register(Comment)
admin.site.register(Product, ProductAdmin)
