from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Person
# Create your views here.
def hello(request):
    return HttpResponse('<html>hello world!</html>')
def list(request):
    l=["css","jquery","javascript","python","django","html"]
    pl=Person.objects.all()
    return render(request,'hello.html',{'list':pl})
