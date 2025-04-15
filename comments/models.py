from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
    

class Trainer(models.Model):
    image = models.ImageField(upload_to='trainers/', default='default.jpg')  # Фото хранятся в /media/products/
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    description = models.TextField(blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)
    stock = models.IntegerField(null=False, blank=False) 


class Product(models.Model): 
    image = models.ImageField(upload_to='products/', default='default.jpg')  # Фото хранятся в /media/products/
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)
    stock = models.IntegerField(null=False, blank=False) 

    def __str__(self):
        return self.name




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связываем корзину с пользователем
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"




class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def get_total_price(self):
        return self.product.price * self.quantity


