from django.shortcuts import render
from subscribe.models import Subscribe


def subscribe(request):
    if request.method == "POST":
        email = request.POST["email"]
        new_subscribe = subscribe()
        new_subscribe.email = email
        new_subscribe.save()

    return render(request, "index.html")
