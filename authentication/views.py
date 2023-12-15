import datetime
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.decorators.http import require_http_methods
from authentication.models import User
from authentication.forms import UserSignUpForm, AdminSignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout
# Create your views here.


class AdminSignUp(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'signup.html'
    success_url = 'frontpage.html'

    def get_context_data(self, **kwargs):
        kwargs['role'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('frontpage:show_frontpage')


class UserSignUp(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'signup.html'
    success_url = 'frontpage.html'

    def get_context_data(self, **kwargs):
        kwargs['role'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('frontpage:show_frontpage')


@require_http_methods(["GET", "POST"])
def login_user(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("frontpage:show_frontpage"))
            date = datetime.datetime.now()
            response.set_cookie('last_login', str(
                date.strftime("%d %B, %Y, %H:%M")))
            return response
        else:
            messages.info(
                request, 'Username atau password salah. Silakan coba lagi.')
    context = {}
    return render(request, 'login.html', context)


@require_http_methods(["GET"])
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('frontpage:show_frontpage'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def login_mobile(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout_mobile(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
