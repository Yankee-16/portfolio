from django import forms
from info.models import Education, Job, Extracurricular


class Eduform(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class Jobform(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class Extraform(forms.ModelForm):
    class Meta:
        model = Extracurricular
        fields = '__all__'
