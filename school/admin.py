from django.contrib import admin

from .models import Course, Registration, Student


# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description', 'level')
    list_display_links = ('id', 'course_code')
    search_fields = ('course_code',)
    list_per_page = 20


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'registration_date', 'period')
    list_display_links = ('id', 'student')
    search_fields = ('student',)
    list_per_page = 20


admin.site.register(Student, StudentsAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)

