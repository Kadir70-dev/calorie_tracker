# tracker/models.py

from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField(default=0)  # Set a default value
    fat = models.FloatField(default=0)    # Set a default value
    print (carbs)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    calories_burned_per_minute = models.FloatField()

    def __str__(self):
        return self.name

class DailyIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name}"

class DailyActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    duration = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.activity.name}"
