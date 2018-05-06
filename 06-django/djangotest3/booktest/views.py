from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return HttpResponse('hello world')


def detail(request, p1, p2, p3):
    return HttpResponse('year:%s, month:%s, day:%s'%( p1, p2 ,p3))


def gettest1(request):
    return render(request, 'booktest/gettest1.html')


def gettest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/gettest2.html', context)


def gettest3(request):
    a1 = request.GET.getlist('a')
    context = {'a': a1}
    return render(request, 'booktest/gettest3.html', context)


def posttest1(request):
    return render(request, 'booktest/posttest1.html')


def posttest2(request):
    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    context = {'username': username, 'password': password, 'gender': gender, 'hobby': hobby}
    return render(request, 'booktest/posttest2.html', context)


def cookietest(request):
    respond = HttpResponse()
    cookie = request.COOKIES
    if 't1' in cookie:
        respond.write(cookie['t1'])
    # respond.set_cookie('t1', 'abc')
    return respond


def redirecttest1(request):
    # return HttpResponseRedirect('redirecttest2')
    return redirect('/booktest/redirecttest2/')

def redirecttest2(request):
    return HttpResponse('redirect page')

def session1(request):
    username = request.session.get('username', 'anonymous')
    context = {'username': username}
    return render(request, 'booktest/session1.html', context)

def session2(request):
    return render(request, 'booktest/session2.html')

def session2_handle(request):
    username = request.POST['username']
    request.session['username'] = username
    request.session.set_expiry(0)
    return redirect('/booktest/session1/')

def session3(request):
    # delete session
    del request.session['username']
    return redirect('/booktest/session1/')
