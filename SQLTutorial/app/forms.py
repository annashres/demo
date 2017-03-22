from django import forms

from .models import Professors, Courses, Students

class ProfessorsForm(forms.ModelForm):
    class Meta:
        model = Professors
        fields = ('firstname', 'lastname', 'email', 'department')

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('name', 'department', 'professor', 'semester', 'year')
    
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('firstname', 'lastname', 'email', 'graduation_year', 'courses')