from django.shortcuts import render

# Create your views here.



def loginAuth(request):
    return render(request, 'auth/login.html')


def registerAuth(request):
    return render(request, 'auth/register.html')


def index(request):
    return render(request, 'dashboard/index.html')