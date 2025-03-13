from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet  # Make sure this is imported correctly

router = DefaultRouter()
router.register(r'home', HomeViewSet)  # Register the ViewSet for GET requests

urlpatterns = [
    path('', include(router.urls)),  
]
