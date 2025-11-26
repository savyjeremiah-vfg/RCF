from django import forms
from .models import Testimony

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['name', 'image', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your testimony...', 'class': 'form-textarea', 'rows': 4}),
        }
