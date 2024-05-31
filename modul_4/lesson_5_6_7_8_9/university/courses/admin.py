from django.contrib import admin
from .models import Speciality, Teacher, Subject
from .forms import SubjectForm


# Register your models here.

# admin.site.register(Speciality)
# admin.site.register(Teacher)
# admin.site.register(Subject)

class SpecialityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']


class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectForm


admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
