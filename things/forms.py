"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class SignUpForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name"]
    
    description = forms.Textarea()
    quantity = forms.NumberInput()
    