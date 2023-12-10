from django.urls import include, path

from authentication.views import UserSignUp, AdminSignUp, login_user, logout_user, login_mobile, logout_mobile, check_is_anonymous, get_user_data

app_name = 'authentication'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('admin-signup/', AdminSignUp.as_view(), name='admin_signup'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('login-mobile/', login_mobile, name='login_mobile'),
    path('logout-mobile/', logout_mobile, name='logout_mobile'),
    path('is-anonymous/', check_is_anonymous, name='check_is_anonymous'),
    path('user-data/', get_user_data, name='get_user_data'),
]
