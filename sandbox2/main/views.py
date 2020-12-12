from django.shortcuts import render, redirect, get_object_or_404
from .models import Requests
from .forms import RequestsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView

class ReqsDetailView(DetailView):
    model = Requests
    template_name = 'main/detail_view.html'
    context_object_name = 'request'

class ReqsUpdateView(UpdateView):
    model = Requests
    template_name = 'main/request_update.html'
    form_class = RequestsForm

@login_required(login_url='login page')
def index(request):
    req = Requests.objects.all()
    return render(request, 'main/index.html', {'req' : req})

@login_required(login_url='login page')
def new_request(request):
    error = ''
    if request.method == 'POST':
        form = RequestsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successful new request')
        else:
            error = 'Неверное заполнение формы'
    form = RequestsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/new_request.html', data)

@login_required(login_url='login page')
def successful_new_request(request):
    return render(request, 'main/successful_new_req.html')

@login_required(login_url='login page')
def my_requests(request):
    req = Requests.objects.all()
    return render(request, 'main/my_requests.html', {'req': req, 'order': [1, 1, 1, 0, 0], 'o': 3, 'do': [1, 1, 0, 0, 0], 'd': 2})

def about(request):
    return render(request, 'main/about.html')
def rules(request):
    return render(request, 'main/rules.html')
def contacts(request):
    return render(request, 'main/contacts.html')
def ofc_info(request):
    return render(request, 'main/ofc_info.html')

@login_required(login_url='login page')
def help(request):
    return render(request, 'main/help.html')

@login_required(login_url='login page')
def feedback(request):
    return render(request, 'main/feedback.html')

@login_required(login_url='login page')
def personal_account(request):
    return render(request, 'main/personal_account.html', {'order': [1, 1, 1, 0, 0], 'o': 3, 'do': [1, 1, 0, 0, 0], 'd': 2})
