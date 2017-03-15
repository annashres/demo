from django import forms

from .models import Reviews

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('course', 'students', 'workload', 'difficulty', 'interest')