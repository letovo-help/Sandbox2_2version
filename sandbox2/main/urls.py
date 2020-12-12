from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all requests'),
    path('<int:pk>', views.ReqsDetailView.as_view(), name='request details'),
    path('<int:pk>/update', views.ReqsUpdateView.as_view(), name='request update'),
    path('new_request', views.new_request, name='new request'),
    path('my_requests', views.my_requests, name='my requests'),
    path('successful_new_request', views.successful_new_request, name='successful new request'),

    path('about', views.about, name='about us'),
path('rules', views.rules, name='rules'),
path('contacts', views.contacts, name='contacts'),
path('ofc_info', views.ofc_info, name='ofc info'),
path('help', views.help, name='help'),
path('feedback', views.feedback, name='feedback'),
path('personal_account', views.personal_account, name='personal account'),
]
