from django import forms
from .models import AppVariety

class AppVarietyForm(forms.Form):
    app_variety = forms.ModelChoiceField(queryset=AppVariety.objects.all(), label="Select the app variety")
