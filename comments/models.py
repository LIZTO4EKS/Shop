from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'


class Product(models.Model): 
    image = models.ImageField(upload_to='products/', blank=False)  # Фото хранятся в /media/products/
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.name