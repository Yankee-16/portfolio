from django.shortcuts import render
from info.models import Education

# Create your views here.
def home(request):
    return render(request, 'info/home.html')

def education(request):
    edu = Education.objects.all()
    dict = {'edu':edu}
    return render(request, 'info/education.html', context=dict)
