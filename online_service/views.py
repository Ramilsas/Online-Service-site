from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, permissions 


from .models import Rolls,Burgers,Pizza,Salads,Sets

from .serializers import RollsSerializer, BurgersSerializer, PizzaSerializer, SaladsSerializer,SetsSerializer

# Create your views here.
class RollsViewSet(viewsets.ModelViewSet):
    queryset = Rolls.objects.all()
    serializer_class = RollsSerializer


class BurgerViewSet(viewsets.ModelViewSet):
    queryset = Burgers.objects.all()
    serializer_class = BurgersSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class SaladsViewSet(viewsets.ModelViewSet):
    queryset = Salads.objects.all()
    serializer_class = SaladsSerializer


class SetsViewSet(viewsets.ModelViewSet):
    queryset = Sets.objects.all()
    serializer_class = SetsSerializer
