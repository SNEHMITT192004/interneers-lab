from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name must be unique
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )  # Price cannot be negative or zero
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])  # Quantity cannot be negative
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

