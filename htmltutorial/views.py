from django.shortcuts import render

# Create your views here.


def htmltutorial(request):
    return render(request, 'htmltutorial.html')