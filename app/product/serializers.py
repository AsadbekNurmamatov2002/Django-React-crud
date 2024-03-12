from rest_framework import serializers
from .models import Product, Tag, Category, Actor


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'