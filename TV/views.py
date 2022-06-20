from django.shortcuts import render

from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import *
def index(request):
     createShow= Show.objects.all()
     context = {
      'createShow': createShow
      }
     return render(request,'index.html',context)


def create(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) >0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/createShow')
        else:
         newShow =Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            RDate=request.POST['Rdate'],

        )
        newShow.save()
    return render(request,'addshow2.html')

def delete(request,_id):
    shows = Show.objects.get(id=_id)
    shows.delete()
    return redirect('/')

def edit(request,_id):
    if request.method == 'GET':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/editeshow4.html')
    else:

        show = Show.objects.get(id=_id)
        context = {
            'show' : show
        }
        return render(request,'editeshow4.html',context)

    if request.method == 'POST':
       print(id)
       show = Show.objects.get(id=_id)
       show.title = request.POST['title']
       show.network=request.POST['network']
       show.save()
       return redirect('/disply/'+_id)


def disply(request,_id):
        show = Show.objects.get(id=_id)
        context = {
            'show' : show

        }
        return render(request, 'displyshow3.html', context)


