"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    
    name = forms.CharField(label="name", max_length=35)
    description = forms.CharField(label = "description", widget=forms.Textarea, max_length=120)
    quantity = forms.CharField(label="quantity", widget=forms.NumberInput)