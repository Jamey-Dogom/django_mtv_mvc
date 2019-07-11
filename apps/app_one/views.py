from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def create(request):
    return index("/")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def show(request, my_val):
    return HttpResponse("placeholder to display blog number {}".format(my_val))

def edit(request, my_val):
    return HttpResponse("place holder to edit blog {}".format(my_val))

def destroy(request, my_val):
    return index("/")