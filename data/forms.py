from django import forms
from .models import Student_cultural, Student_sports, Student_technical

class StudentFormCultural(forms.ModelForm):
    intercollege_mcq = forms.BooleanField(label='Intercollege', required=False)
    intracollege_mcq = forms.BooleanField(label='Intracollege', required=False)
    
    class Meta:
        model = Student_cultural
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description',
                  'event_type', 'intercollege_mcq', 'intracollege_mcq',
                  'position', 'certificate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'certificate': forms.FileInput(attrs={'class': 'form-control'}),
        }

class StudentFormSports(forms.ModelForm):
    intercollege_mcq = forms.BooleanField(label='Intercollege', required=False)
    intracollege_mcq = forms.BooleanField(label='Intracollege', required=False)
    
    class Meta:
        model = Student_sports
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description',
                  'event_type', 'intercollege_mcq', 'intracollege_mcq',
                  'position', 'certificate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'certificate': forms.FileInput(attrs={'class': 'form-control'}),
        }

class StudentFormTechnical(forms.ModelForm):
    intercollege_mcq = forms.BooleanField(label='Intercollege', required=False)
    intracollege_mcq = forms.BooleanField(label='Intracollege', required=False)
    
    class Meta:
        model = Student_technical
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description',
                  'event_type', 'intercollege_mcq', 'intracollege_mcq',
                  'position', 'certificate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'certificate': forms.FileInput(attrs={'class': 'form-control'}),
        }
