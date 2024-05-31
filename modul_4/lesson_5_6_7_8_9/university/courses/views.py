from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from dal import autocomplete
from .forms import SpecialityForm, TeacherForm, SubjectForm
from .models import Speciality, Teacher, Subject


def course_name_view(request):
    name = request.GET.get('name', 'Django')
    return HttpResponse(f"Hello {name}")


def speciality_list_view(request):
    specialities = Speciality.objects.all()
    if not specialities:
        message = "No speciality"
        return render(request, 'speciality_list.html', {'message': message})
    return render(request, 'speciality_list.html', {'specialities': specialities})


def teacher_search_view(request):
    search = request.GET.get('search', '')
    if not search:
        message = "No search"
        return render(request, 'teacher_search.html', {'message': message})

    teachers = Teacher.objects.filter(first_name__icontains=search)
    if not teachers.exists():
        message = "No teachers"
        return render(request, 'teacher_search.html', {'message': message})

    return render(request, 'teacher_search.html', {'teachers': teachers})


def subject_list_view(request):
    subjects = Subject.objects.all()
    if not subjects:
        message = "No subjects"
        return render(request, 'subjects_list.html', {'message': message})
    return render(request, 'subjects_list.html', {'subjects': subjects})


def subject_detail_view(request, id):
    subject = get_object_or_404(Subject, id=id)
    return render(request, 'subject_detail.html', {'subject': subject})


def speciality_create(request):
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('speciality_list_view')
    else:
        form = SpecialityForm()
    return render(request, 'speciality_form.html', {'form': form})


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list_view')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})


def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list_view')
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})


class SpecialityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Speciality.objects.none()
        qs = Speciality.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class TeacherAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Teacher.objects.none()
        qs = Teacher.objects.all()
        if self.q:
            qs = qs.filter(first_name__icontains=self.q)
        return qs
