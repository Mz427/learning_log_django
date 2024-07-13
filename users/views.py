from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        print(form)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("python_django_NFSs:index")
    context= {"form": form}
    return render(request, "registration/register.html", context)