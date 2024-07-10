from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelWithFileField
import os

# Create your views here.
def index(request):
    return render(request, 'python_django_NFSs/index.html')

def list_files(request, dir_name):
    if request.method == "GET":
        dir_path = f"/home/mz/{dir_name}/"
        files_attribute = {}
        for i in os.listdir(dir_path):
            if os.path.isdir(dir_path + i):
                files_attribute[i] = "dir"
            else:
                files_attribute[i] = "file"
        return render(request, "python_django_NFSs/list_files.html", {"files_attribute": files_attribute})
    elif request.method == "POST":
        upload_files = request.FILES.get("upload_files")
        ModelWithFileField(path=upload_files).save()
        return HttpResponse("Success!")