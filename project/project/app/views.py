from django.shortcuts import render
from django.shortcuts import HttpResponse
def hello_world(request):
    return render(request,'task.html')

# Create your views here.
