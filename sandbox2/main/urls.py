from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all requests'),
    path('about', views.about, name='about us'),
    path('new_request', views.new_request, name='new request'),
    path('successful_new_request', views.successful_new_request, name='successful new request'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)