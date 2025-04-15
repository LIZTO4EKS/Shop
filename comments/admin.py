from django.contrib import admin
from .models import Comment, Product, Trainer, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image') 
    search_fields = ('name',)  
    list_filter = ('price',)
    

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image') 
    search_fields = ('name',)  
    list_filter = ('price',)
    
    
    

admin.site.register(Comment)
admin.site.register(CartItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(Trainer, TrainerAdmin)
