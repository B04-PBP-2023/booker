from django.shortcuts import render
from book.forms import BookForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.


@csrf_exempt
@login_required(login_url='/authentication/login/')
def show_donasi_buku(request):
    form = BookForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        book = form.save(commit=False)
        book.for_sale = False
        book.save()
        user = request.user
        user.points += 50
        user.save()
        return HttpResponseRedirect(reverse('frontpage:show_frontpage'))

    context = {
        'form': form
    }
    return render(request, "donasibuku.html", context)


@csrf_exempt
@login_required(login_url='/authentication/login/')
def donasi_buku_mobile(request):
    form = BookForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        book = form.save(commit=False)
        book.for_sale = False
        book.save()
        user = request.user
        user.points += 50
        user.save()
        return JsonResponse({
            "success": True,
        }, status=201)

    return JsonResponse({
        "success": False,
    }, status=301)
