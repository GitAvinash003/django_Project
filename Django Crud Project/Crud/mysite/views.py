from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Inserted details successfully")
            return redirect('/index/')
    else:
        form=StudentForm()   
    obj = Student.objects.all()    
    return render(request,'index.html',{'frm':form,'obj':obj,})

#destroy
def delete(request, id):
  member = Student.objects.get(id=id)
  member.delete()
  messages.error(request,"Deleted details successfully")
  return HttpResponseRedirect(reverse('index'))

def edit(request,id):
    obj=Student.objects.get(id=id)
    return render(request,'edit.html', {'obj':obj})  
    
def update(request,id):
    obj=Student.objects.get(id=id)
    form = StudentForm(request.POST, instance =obj)  
    if form.is_valid():
        form.save()
        return redirect("/index")  
    return render(request, 'edit.html', {'obj':obj})  

