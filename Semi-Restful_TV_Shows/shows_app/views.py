from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

def shows(request):
    context = {
        'Shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def create(request):

    Show.objects.create (
            Title=request.POST['title'], 
            Network=request.POST['network'], 
            Release_Date=request.POST['release_date'],
            Description=request.POST['description'],
    )
    return redirect ('/')

def new_show(request):
    return render(request, "new.html")

def edit_show(request, id):
    context = {
        'Show' : Show.objects.get(id=id)
    }
    return render(request, "editshow.html", context)

def update(request, id):
    
    show = Show.objects.get(id=id)
    show.Title = request.POST.get('title')
    show.Network=request.POST.get('network')
    show.Description= request.POST.get('description')
    show.save ()
    return redirect ('/')

def show_profile(request, id):
    context={
        'Show': Show.objects.get(id= id)
        
    }
    return render(request, "profile.html", context)

def destroy(request, id):
    show = Show.objects.get(id= id)
    show.delete()
    return redirect ('/')

