from django.urls import path
from .views import CustomUserLogin,CustomUserSignup, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('', CustomUserLogin.as_view(), name="login"),
    path('sign_up/', CustomUserSignup.as_view(), name="sign_up"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]