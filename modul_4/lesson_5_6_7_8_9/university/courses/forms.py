from django import forms
from .models import Speciality, Teacher, Subject
from dal import autocomplete


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
    specialities = forms.ModelMultipleChoiceField(
        queryset=Speciality.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='speciality-autocomplete')
    )
    teachers = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='teacher-autocomplete')
    )

    class Meta:
        model = Subject
        fields = ['name', 'specialities', 'teachers']
