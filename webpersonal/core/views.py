from django.shortcuts import render, HttpResponse

# Create your views here.

def home(resquest):
    return render(resquest, "core/home.html")

def about(resquest):
    return render(resquest, "core/about.html")



def contact(resquest):
    return render(resquest, "core/contact.html")