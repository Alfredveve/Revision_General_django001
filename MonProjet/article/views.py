from django.shortcuts import render
from django.http import HttpResponse

def index(request, *args, **kw):
    text = "<h2> Je fais une grande revision 001 dans django</h2>"
    return HttpResponse(text)
