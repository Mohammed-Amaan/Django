from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("hello world i am home")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("hello,this is the about page")
    return render(request,'about.html')
