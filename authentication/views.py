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
from django.http import HttpResponse
from django.core import serializers
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
