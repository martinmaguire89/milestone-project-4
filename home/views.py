from django.shortcuts import render


def index(request):
    """a view that dispalys the index page"""
    return render(request, "index.html")
