from django.shortcuts import render ,redirect
from .models import *

def home(request):
	return render(request,'index.html')

def username(request):
    if request.method == 'POST':
        UserId = request.POST['UserID']
        user = UserName.objects.get(id = UserId)
        user.Username = request.POST['Username']
       