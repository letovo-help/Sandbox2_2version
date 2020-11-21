from django.shortcuts import render, redirect
from .models import Requests
from .forms import RequestsForm
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

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


def successful_new_request(request):
    return render(request, 'main/successful_new_req.html')