from django.urls import path
from .views import FoodItemListCreate, FoodItemRetrieveUpdateDestroy

urlpatterns = [
    path('food-items/', FoodItemListCreate.as_view(), name='fooditem-list-create'),
    path('food-items/<int:pk>/', FoodItemRetrieveUpdateDestroy.as_view(), name='fooditem-rud'),
]
