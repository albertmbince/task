from django import forms
from .models import details
class detailsForm(forms.ModelForm):
    class Meta:
        model = details
        fields = "__all__"