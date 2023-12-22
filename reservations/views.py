from django.shortcuts import get_object_or_404, redirect, render
from .forms import SubjectForm
from .models import Subject, Teacher
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def subject_list(req):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(req, 'subject_list.html', context)

@login_required(login_url='login')
def subject_create(req):
    form = SubjectForm(req.POST or None)
    if form.is_valid():
        form.save()
        messages.success(req, 'Ders başarılı bir şekilde eklendi.')
        return redirect('subjects')
    
    context = {'form': form}
    return render(req, 'subject_create.html', context)

@login_required(login_url='login')
def subject_update(req, id):
    subject = get_object_or_404(Subject, id = id)
    form =  SubjectForm(req.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        messages.success(req, 'Ders başarılı bir şekilde güncellendi.')
        return redirect('subjects')
    context = {
        'form': form
    }
    return render(req,'subject_update.html', context)

@login_required(login_url='login')
def subject_delete(req, id):
    subject = get_object_or_404(Subject, id = id)
 
    if req.method =="POST":
        subject.delete()
        messages.success(req, 'Ders başarılı bir şekilde silindi.')
        return redirect('subjects')
    
    return render(req, 'subject_delete.html')