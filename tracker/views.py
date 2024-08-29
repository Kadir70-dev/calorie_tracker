from rest_framework import generics
from .models import FoodItem
from .serializers import FoodItemSerializer

class FoodItemListCreate(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class FoodItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
