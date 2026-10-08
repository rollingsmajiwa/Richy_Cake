from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Cake(models.Model):
    image = CloudinaryField("image")
    name = models.TextField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey('Cake', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.cake.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.cake.name} ({self.user.username})"


