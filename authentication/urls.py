from django.urls import include, path

from authentication.views import UserSignUp, AdminSignUp, login_user, logout_user, login_mobile

app_name = 'authentication'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('admin-signup/', AdminSignUp.as_view(), name='admin_signup'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('login-mobile/', login_mobile, name='login_mobile'),
]
