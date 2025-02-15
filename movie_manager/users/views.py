from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signup(request):

    user=None
    error_message=None

    if request.POST:

        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message=str(e)

    return render(request,'users/create.html',{'user':user,'error_message':error_message})