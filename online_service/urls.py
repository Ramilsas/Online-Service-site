from django.urls import path, re_path, include
from rest_framework import routers
from .views import RollsViewSet, BurgerViewSet, PizzaViewSet, SaladsViewSet, SetsViewSet


app_name = 'online_service'

router = routers.DefaultRouter()

router.register(r'Rolls-ViewSet', RollsViewSet, basename='rolls-viewset')
router.register(r'Burger-ViewSet', BurgerViewSet, basename='burger-viewset')
router.register(r'Pizza-ViewSet', PizzaViewSet, basename='pizza-viewset')
router.register(r'Salads-ViewSet', SaladsViewSet, basename='salads-viewset')
router.register(r'Sets-ViewSet', SetsViewSet, basename='sets-viewset')



urlpatterns = [
    path('', include(router.urls)),

]








