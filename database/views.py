from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from database.models import addUser

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        adduser = addUser(name=name, password=password, date=datetime.today())
        adduser.save()
    
    return render(request, 'index.html')

