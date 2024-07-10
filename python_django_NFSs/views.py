from django.shortcuts import render
from django.http import HttpResponseRedirect
import os

# Create your views here.
def index(request):
    return render(request, 'python_django_NFSs/index.html')

def list_files(request, dir_name):
    dir_path = f"/home/mz/{dir_name}/"
    files_attribute = {}
    for i in os.listdir(dir_path):
        if os.path.isdir(dir_path + i):
            files_attribute[i] = "dir"
        else:
            files_attribute[i] = "file"

    return render(request, "python_django_NFSs/list_files.html", {"files_attribute": files_attribute, "cwd": dir_name})