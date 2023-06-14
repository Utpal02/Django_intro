# i created this file - Utpal Tiwari

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>HOME</h1>")

def removepunc(request):
    return HttpResponse("remove punc")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("character count")

def newlineremove(request):
    return HttpResponse("newline remove")

def capfirst(request):
    return HttpResponse("capitalize first")