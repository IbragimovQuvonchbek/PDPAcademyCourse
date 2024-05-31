from django.urls import path
from .views import teacher_create, subject_detail_view, subject_list_view, course_name_view, speciality_list_view, \
    teacher_search_view, \
    speciality_create, subject_create

urlpatterns = [
    path('', course_name_view, name='course_name_view'),
    path('speciality/', speciality_list_view, name='speciality_list_view'),
    path('teacher/', teacher_search_view, name='teacher_search_view'),
    path('subject/', subject_list_view, name='subject_list_view'),
    path('subject/<int:id>/', subject_detail_view, name='subject_detail_view'),
    path('speciality/create/', speciality_create, name='speciality_create'),
    path('teacher/create/', teacher_create, name='teacher_create'),
    path('subject/create/', subject_create, name='subject_create'),
]
