from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def new(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc = request.POST['desc'])
        messages.success(request, "Show successfully added")
        return redirect ("/shows") 

def show(request):                
    context = {"shows": Show.objects.all()}
    return render(request, "show/show.html", context)                                

def index(request):                
    # context = {"shows": Show.objects.all()}
    return render(request, "show/index.html")                                

def show_one(request,id):
    context = {"show": Show.objects.get(id = id)}
    return render(request, "show/showOne.html", context)

def editShow(request, id):                
    context = {"shows": Show.objects.get(id=id)}
    return render(request, "show/editShow.html", context)    

def editShowFunction(request,id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        u = Show.objects.get(id = id)
        u.title=request.POST['title']
        u.network=request.POST['network']
        u.release_date=request.POST['release_date']
        u.desc = request.POST['desc']
        u.save()
        messages.success(request, "Blog successfully updated")
        return redirect ("/shows")

def delete(request,id):
    d = Show.objects.get(id = id)
    d.delete()
    return redirect ("/shows")

