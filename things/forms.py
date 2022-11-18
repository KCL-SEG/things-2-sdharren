"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name"]
    
    description = forms.Textarea(label = "Description")
    quantity = forms.NumberInput(label = "Quantity")    