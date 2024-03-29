# Flake8: noqa
"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from school.views import (CourseViewSet, ListRegistrationStudents,
                          ListStudentsCouses, RegistrationViewSet,
                          StudentViewSet)

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='Course')
router.register(r'students', StudentViewSet, basename='Student')
router.register(r'registrations', RegistrationViewSet, basename='Registration')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', ListRegistrationStudents.as_view(), name='list_registration_students'),
    path('courses/<int:pk>/registrations/', ListStudentsCouses.as_view(), name='list_students_courses'),
]
