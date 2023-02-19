from rest_framework import serializers

from .models import Rolls,Burgers,Pizza,Salads,Sets

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')


class RollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rolls
        fields = ('__all__')


class BurgersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burgers
        fields = ('__all__')


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('__all__')


class SaladsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salads
        fields = ('__all__')

class SetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sets
        fields = ('__all__')
