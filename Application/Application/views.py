#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url="/users/login/")
def get_username(request):
    if request.user.is_authenticated:
        return {'username': request.user.username}
    return {'username': None}



def about(request):
    return render(request, 'about.html')

def landing_page(request):
    return render(request, 'landing_page.html')

