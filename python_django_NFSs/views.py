from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'python_django_NFSs/index.html')