from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os

# Create your views here.
def index(request):
    return render(request, 'python_django_NFSs/index.html')

def files_management(request, dir_name):
    dir_path = f"/home/mz/{dir_name}/"
    if request.method == "GET":
        files_attribute = {}
        for i in os.listdir(dir_path):
            if os.path.isdir(dir_path + i):
                files_attribute[i] = "dir"
            else:
                files_attribute[i] = "file"
        return render(request, "python_django_NFSs/files_management.html", {"files_attribute": files_attribute, "cwd": dir_name + "/"})
    elif request.method == "POST":
        if request.POST["submit"] == "Download":
            for i, j in request.POST.items():
                if j in ("file", "dir"):
                    if i != "":
                        print(i)
                        # with open(f"{dir_path}{i}", "rb") as file_downloaded:
                        file_downloaded = open(f"{dir_path}{i}", "rb") 
                        return FileResponse(file_downloaded, as_attachment=True)
        elif request.POST["submit"] == "Upload":
            upload_files = request.FILES["upload_files"]
            with open(f"{dir_path}{upload_files.name}", "wb+") as file_uploaded:
                for chunk in upload_files.chunks():
                    file_uploaded.write(chunk)
            return HttpResponse("The file upload successfully!")
        elif request.POST["submit"] == "Delete":
            return HttpResponse("The file Delete successfully!")
        elif request.POST["submit"] == "Rename":
            return HttpResponse("The file Rename successfully!")