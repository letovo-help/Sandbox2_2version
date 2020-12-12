from django.shortcuts import render, redirect
from .models import Requests
from .forms import RequestsForm
from .models import Requests
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView

class ReqsDetailView(DetailView):
    model = Requests
    template_name = 'main/detail_view.html'
    context_object_name = 'request'

class ReqsUpdateView(UpdateView):
    model = Requests
    template_name = 'main/request_update.html'
    form_class = RequestsForm


def index(request):
    req = Requests.objects.all()
    return render(request, 'main/index.html', {'req' : req})

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


def successful_new_request(request):
    return render(request, 'main/successful_new_req.html')

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
def help(request):
    return render(request, 'main/help.html')
def feedback(request):
    return render(request, 'main/feedback.html')
def personal_account(request):
    return render(request, 'main/personal_account.html', {'order': [1, 1, 1, 0, 0], 'o': 3, 'do': [1, 1, 0, 0, 0], 'd': 2})
