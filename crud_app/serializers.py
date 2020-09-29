from rest_framework import serializers
from . models import Crud


class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = ('id', 'title', 'description', 'published')

    def create(self, validated_data):
        return Crud.objects.create(**validated_data)
