from django.http import HttpResponse

def index():
    return HttpResponse('hello world 2')