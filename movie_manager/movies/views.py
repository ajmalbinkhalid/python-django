from django.shortcuts import render
from . models import MovieInfo

# Create your views here.

from . forms import MovieForm

def create(request):
    
    if request.POST:
         
         frm=MovieForm(request.POST,request.FILES)
         if frm.is_valid():
              frm.save()
    else:     
         frm=MovieForm()
    return render(request,'create.html',{'frm': frm})

def list(request):
        print(request.COOKIES)
        visits=int(request.COOKIES.get('visits',0))
        visits=visits+1
        movie_set=MovieInfo.objects.filter(title__startswith='j')
        print(movie_set)
        response=render(request,'list.html',{'movies': movie_set,'visits':visits})
        response.set_cookie('visits',visits)
        return response

def edit(request,pk):
     instance_to_be_edited=MovieInfo.objects.get(pk=pk)
     if request.POST:
       frm=MovieForm(request.POST,instance=instance_to_be_edited)
       if frm.is_valid():
             instance_to_be_edited.save()
     else:
         frm=MovieForm(instance=instance_to_be_edited)         
          
   
     frm=MovieForm(instance=instance_to_be_edited)

     return render(request,'create.html',{'frm': frm})

def delete(request,pk):
        instance=MovieInfo.objects.get(pk=pk)
        instance.delete()

        movie_set=MovieInfo.objects.all()
        print(movie_set)
     
        return render(request,'list.html',{'movies': movie_set})
