from rest_framework import serializers
from .models import *


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    mark = MarkSerializer()
    class Meta:
        model = Student
        fields = '__all__'