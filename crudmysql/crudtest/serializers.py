from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ['url', 'id', 'first_name', 'last_name', 'middle_name', 'gender', 'age']