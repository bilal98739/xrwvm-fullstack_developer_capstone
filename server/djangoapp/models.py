from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# -----------------------------
# CarMake Model
# -----------------------------
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name


# -----------------------------
# CarModel Model
# -----------------------------
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relation
    dealer_id = models.IntegerField(blank=True, null=True)  # <-- Fixed: allow NULL values
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    current_year = datetime.date.today().year
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(current_year)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"


# Optional: Add a helper method if you ever need to filter models
# Example:
# CarModel.objects.filter(car_make__name="Toyota")
