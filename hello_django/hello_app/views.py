from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={ 'movies' : [{
        'title':'Godfather',
        'year':1990,
        'success':True
        },
        {
        'title':'Marco',
        'year':2024,
        'summary':'story of an underworld family in gold business',
        'success':True
        },
        {
        'title':'Avesham',
        'year':2024,
        'summary':'story of a one man gangster and college students friendship',
        'success':True
        }
    ]}

    return render(request,'hello.html',movie_data)
