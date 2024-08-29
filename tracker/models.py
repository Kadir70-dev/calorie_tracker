from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date_consumed = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.calories} calories"