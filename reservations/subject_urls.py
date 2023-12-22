from django.urls import path
from .views import *

urlpatterns = [
    path('', subject_list, name='subjects'),
    path('create', subject_create, name='subject_create'),
    path('<int:id>/update', subject_update, name='subject_update'),
    path('<int:id>/delete', subject_delete, name='subject_delete'),
]