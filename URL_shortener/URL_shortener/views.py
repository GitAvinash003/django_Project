from django.shortcuts import render  #import render
from django.http import HttpResponse #import https respose file

def aboutus(request):
    return HttpResponse("hello world i am in django framework")
def course(request):
    return HttpResponse("this is course page")
def helloworld(request):
    return HttpResponse("helllo wolrd!")    # create function for request