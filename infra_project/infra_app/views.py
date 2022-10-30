from django.http import HttpResponse


def index(request):
    return HttpResponse('ПОШЕЛ НА ХУЙ')


def second_page(request):
    return HttpResponse('А это вторая страница!')
