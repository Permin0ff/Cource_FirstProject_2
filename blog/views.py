from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")


def products(request):
    return HttpResponse("Список товаров")


def new(request):
    return HttpResponse("Новые товары")


def top(request):
    return HttpResponse("Наиболее популярные товары")