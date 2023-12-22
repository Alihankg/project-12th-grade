from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Öğretmen Adı ve Soyadı')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='teachers')

class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ders Adı')

    def __str__(self):
        return self.name