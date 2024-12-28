# Views file is like Controllers in MVC architecture. It is responsible for handling the requests and responses.

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You're at the chaiaurdjango home page.")
    return render(request, 'website/index.html', {})

def about(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango contact page.")