from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.

def index(request):
    # hero = HeroInfo.objects.get(pk__exact=1)
    # context = {'hero': hero}

    list = HeroInfo.objects.all()
    # list = HeroInfo.objects.filter(isDelete=True)
    context = {'list': list}
    return render(request, 'booktest/index.html', context)


def show(request, id, id2):
    context = {'id': id}
    return render(request, 'booktest/show.html', context)


def index2(request):
    return render(request, 'booktest/index2.html')


def user1(request):
    return render(request, 'booktest/user1.html')


def user2(request):
    return render(request, 'booktest/user2.html')


def htmltest(request):
    context={'t1': '<h1>hello</h1>'}
    return render(request, 'booktest/htmltest.html', context)


def csrf1(request):
    return render(request,'booktest/csrf1.html')


def csrf2(request):
    username = request.POST['username']
    return HttpResponse(username)


def verifycode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random

    bgcolor = (random.randrange(50,100),random.randrange(50, 100), 0)
    width = 100
    height = 25

    image = Image.new('RGB',(width, height), bgcolor)
    font = ImageFont.truetype('FreeMono.ttf', 23)
    draw = ImageDraw.Draw(image)
    text = '0123abcd'
    texttemp = ''
    for i in range(4):
        texttemp1 = text[random.randrange(0, len(text))];
        texttemp+= texttemp1
        draw.text((i*25,0),
                  texttemp1,
                  (255,255,255),
                  font)
    request.session['code'] = texttemp
    # draw.text((0,0), text, (255,255,255), font)
    from io import BytesIO
    buf = BytesIO()
    image.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')

def verifytest1(request):
    return render(request, 'booktest/verifytest1.html')


def verifytest2(request):
    code1 = request.POST['code1']
    code2 = request.session['code']

    if code1 == code2:
        return HttpResponse('ok')
    else:
        return HttpResponse('fail')
