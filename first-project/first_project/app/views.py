from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.today().strtime('%H:%M:%S')
    return HttpResponse(f'Текущее время: {current_time}')

def workdir_view(request):
    files_project = os.listdir(os.getcwd())
    return HttpResponse(f'Список файлов рабочей директории: {files_project}')


