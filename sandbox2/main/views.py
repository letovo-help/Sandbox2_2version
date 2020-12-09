from django.shortcuts import render, redirect
from .models import Requests
from .forms import RequestsForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login page')
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

@login_required(login_url='login page')
def new_request(request):
    #req = Requests.objects.all()
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