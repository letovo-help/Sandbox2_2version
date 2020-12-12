from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from account.views import PasswordResetTokenView

urlpatterns = [
    path('login', views.loginPage, name='login page'),
    path('register', views.register, name='register page'),
    path('logout', views.logoutUser, name='logout'),
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    url(r"^account/", include("account.urls")),
]

"""urlpatterns = [
    url(r"^account/login/$", views.LoginView.as_view(), name="account_login"),
    url(r"^account/signup/$", views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r"^account/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
]"""