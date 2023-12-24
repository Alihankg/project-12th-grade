from django.shortcuts import get_object_or_404, redirect, render
from .forms import SubjectForm
from .models import Subject, Teacher
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def subject_list(req):
    subjects = Subject.objects.all()
    subject_form = SubjectForm()
    context = {
        'subjects': subjects,
        'form': subject_form,
    }
    return render(req, 'subject_list.html', context)

@login_required(login_url='login')
def subject_create(req):
    form = SubjectForm(req.POST or None)
    if form.is_valid():
        form.save()
        messages.success(req, 'Ders başarılı bir şekilde eklendi.')
        return redirect('subjects')

@login_required(login_url='login')
def subject_update(req, id):
    subject = get_object_or_404(Subject, id = id)
    form = SubjectForm(req.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        messages.success(req, 'Ders başarılı bir şekilde güncellendi.')
        return redirect('subjects')

@login_required(login_url='login')
def subject_delete(req, id):
    subject = get_object_or_404(Subject, id = id)
    subject.delete()
    messages.success(req, 'Ders başarılı bir şekilde silindi.')
    return redirect('subjects')