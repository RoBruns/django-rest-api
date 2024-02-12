from rest_framework import viewsets

from .models import Course, Registration, Student
from .serializer import (CourseSerializer, RegistrationSerializer,
                         StudentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registrations to be viewed or edited.
    """
    queryset = Registration.objects.all().order_by('id')
    serializer_class = RegistrationSerializer