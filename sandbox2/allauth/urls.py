from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from account.views import PasswordResetTokenView

urlpatterns = [
    path('login', views.loginPage, name='login page'),
    path('register', views.register, name='register page'),
    path('logout', views.logoutUser, name='logout'),
    url(r"^account/", include("account.urls")),
]

"""urlpatterns = [
    url(r"^account/login/$", views.LoginView.as_view(), name="account_login"),
    url(r"^account/signup/$", views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r"^account/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
]"""