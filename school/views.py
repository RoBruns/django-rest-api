from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Course, Registration, Student
from .serializer import (CourseSerializer, ListRegistrationStudentsSerializer,
                         ListStudentsCousesSerializer, RegistrationSerializer,
                         StudentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registrations to be viewed or edited.
    """
    queryset = Registration.objects.all().order_by('id')
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListRegistrationStudents(generics.ListAPIView):
    """
    API endpoint that allows registrations to be viewed.
    """
    serializer_class = ListRegistrationStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset


class ListStudentsCouses(generics.ListAPIView):
    """
    API endpoint that allows registrations to be viewed.
    """
    serializer_class = ListStudentsCousesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
