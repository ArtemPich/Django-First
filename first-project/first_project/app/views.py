from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = None
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    workdir = None
    msg = f'Содержимое рабочей директории: {workdir}'
    return HttpResponse(msg)

    raise NotImplemented
