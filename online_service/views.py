from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins, generics, permissions 

from .models import Product, Cart, CartItem

from .models import Rolls,Burgers,Pizza,Salads,Sets, Drinks, Product

from .serializers import RollsSerializer, BurgersSerializer, PizzaSerializer, SaladsSerializer,SetsSerializer,\
    DrinksSerializer, ProductSerializer

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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer



def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Проверяем, есть ли корзина в сессии пользователя
    if 'cart_id' in request.session:
        cart = Cart.objects.get(id=request.session['cart_id'])
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    # Проверяем, есть ли товар в корзине
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart=cart, product=product, quantity=1)

    return redirect('cart')
