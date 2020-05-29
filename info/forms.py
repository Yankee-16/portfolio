from django import forms
from info.models import Education


class Eduform(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
