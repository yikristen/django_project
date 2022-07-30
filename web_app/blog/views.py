from django.shortcuts import render
from django.http improt HttpResponse

#new function to handle traffic between homepage and blog
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
def about(request):
     return HttpResponse('<h1>Blog About</h1>')
