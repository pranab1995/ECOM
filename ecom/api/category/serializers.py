from rest_framework import serializers

from .models import Category

class CategorySeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')