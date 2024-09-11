# tracker/serializers.py

from rest_framework import serializers
from .models import FoodItem, Activity, DailyIntake, DailyActivity

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class DailyIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyIntake
        fields = '__all__'

class DailyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyActivity
        fields = '__all__'
