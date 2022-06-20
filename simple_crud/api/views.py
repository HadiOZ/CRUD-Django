from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def create(request: HttpRequest):
  path = request.get_full_path()
  return HttpResponse("ada melakukan request ke path {}".format(path))

def read(request: HttpRequest):
  path = request.get_full_path()
  return HttpResponse("ada melakukan request ke path {}".format(path))

def update(request: HttpRequest):
  path = request.get_full_path()
  return HttpResponse("ada melakukan request ke path {}".format(path))

def delete(request: HttpRequest):
  path = request.get_full_path()
  return HttpResponse("ada melakukan request ke path {}".format(path))

# def create(request):
  
#   return HttpResponse()