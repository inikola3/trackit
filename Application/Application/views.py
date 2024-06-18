#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def homepage(request):
   return render(request, 'home.html', {'username': request.user.username.capitalize()})

def about(request):
    return render(request, 'about.html')


def landing_page(request):
    return render(request, 'landing_page.html')

