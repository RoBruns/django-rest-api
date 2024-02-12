from rest_framework import serializers

from .models import Course, Registration, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []


class ListRegistrationStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['course', 'period']
        depth = 1
