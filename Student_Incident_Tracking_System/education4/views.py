from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# ========== index =========

def index(request):
    template = 'index.html'
    return render(request,template)
