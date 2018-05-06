from django.shortcuts import render
from .models import *
from django.db.models import Max,F,Q

# Create your views here.

def index(request):
    # list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    # Max = BookInfo.books1.aggregate(Max('bpub_date'))
    # list = BookInfo.books1.filter(bread__gt=F('bcomment'))
    # list = BookInfo.books1.filter(pk__lt=4, btitle__contains='1')
    # list = BookInfo.books1.filter(pk__lt=4, btitle__contains='1')
    list = BookInfo.books1.filter(Q(pk__lt=4) | Q(btitle__contains='1'))
    context = {'list': list,
               # 'Max': Max1
               }
    return render(request, 'booktest/index.html', context)
