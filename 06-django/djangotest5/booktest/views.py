from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from .models import *
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .task import *

# Create your views here.

def index(request):
    return render(request, 'booktest/index.html')

def myExp(request):
    return HttpResponse('Hello')

def uploadpic(request):
    return render(request, 'booktest/uploadpic.html')

def uploadhandle(request):
    pic1 = request.FILES['pic1']
    picname = os.path.join(settings.MEDIA_ROOT,pic1.name)

    with open(picname, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)

    return HttpResponse('<img src="/static/media/%s"/>'%pic1.name)


def herolist(request, pindex):
    print(pindex)
    if pindex == '':
        pindex = '1'
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 5)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest/herolist.html', context)


def area(request):
    return render(request, 'booktest/area.html')


def area2(request, id):
    id1 = int(id)
    # province
    if id1 == 0:
        data = AreaInfo.objects.filter(parea__isnull = True)
    else:
        data = AreaInfo.objects.filter(parea_id = id)
    list = []
    for area in data:
        list.append({'id':area.id, 'title': area.title})

    return JsonResponse({'data':list})

def htmleditor(request):
    return render(request, 'booktest/htmleditor.html')

def htmleditorhandle(request):
    html = request.POST['hcontent']
    tinyinfo1 = TinyInfo.objects.get(pk=1)
    tinyinfo1.content = html
    tinyinfo1.save()
    content = {'content': html}
    return render(request, 'booktest/htmlshow.html', content)

@cache_page(60*10)
def cache1(request):
    return HttpResponse('hello world!')


def cache2(request):
    cache.set('key1', 'value1', 600)
    print(cache.get('key1'))
    # cache.clear()
    return render(request, 'booktest/cachetest.html')


def mysearch(request):
    return render(request,'booktest/mysearch.html')


# celery
def celerytest(request):
    # show()
    show.delay()
    return HttpResponse('ok')


