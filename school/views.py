from rest_framework import generics, viewsets

from .models import Course, Registration, Student
from .serializer import (CourseSerializer, ListRegistrationStudentsSerializer,
                         RegistrationSerializer, StudentSerializer)


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


class ListRegistrationStudents(generics.ListAPIView):
    """
    API endpoint that allows registrations to be viewed.
    """
    serializer_class = ListRegistrationStudentsSerializer

    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset


