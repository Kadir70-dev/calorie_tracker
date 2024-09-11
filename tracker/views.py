# tracker/views.py

from rest_framework import viewsets
from .models import FoodItem, Activity, DailyIntake, DailyActivity
from .serializers import FoodItemSerializer, ActivitySerializer, DailyIntakeSerializer, DailyActivitySerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class DailyIntakeViewSet(viewsets.ModelViewSet):
    queryset = DailyIntake.objects.all()
    serializer_class = DailyIntakeSerializer

class DailyActivityViewSet(viewsets.ModelViewSet):
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializer
