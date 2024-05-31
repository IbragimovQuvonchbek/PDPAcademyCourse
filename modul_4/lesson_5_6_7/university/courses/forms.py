from django import forms
from .models import Speciality, Teacher, Subject


class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
