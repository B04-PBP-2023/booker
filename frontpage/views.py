from django.shortcuts import render

# Create your views here.


def show_frontpage(request):
    context = {}
    return render(request, "frontpage.html", context)
