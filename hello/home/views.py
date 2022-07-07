#from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request) :
    return HttpResponse("hello this is the home page of the website")

def home(request) :
    return HttpResponse("hello this is the home page")
def about(request) :
    return HttpResponse("hello this is the about  page")
def default(request) :
    context = {
        "variable" : "this is a variable", "variable2" : "this is the second variable"
    }
    #return HttpResponse("you are at the default page of my website to go to about page add /about in the web address or add /home ")
    return render(request , "test.html", context)