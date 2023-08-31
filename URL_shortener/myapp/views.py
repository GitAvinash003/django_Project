from django.shortcuts import render #page load
from django.http import HttpResponse  #for string load

    
# Create your views here.
def home_page(request):
   return render( request,"index.html") 
