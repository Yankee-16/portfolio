from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'info/home.html')

def education(request):
    return render(request, 'info/education.html')
