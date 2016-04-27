from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('<html>hello world!</html>')
def list(request):
    l=["css","jquery","javascript","python","django","html"]
    return render(request,'hello.html',{'list':l})
