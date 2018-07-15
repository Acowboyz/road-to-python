from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page

# Create your views here.

def index(request):
    # 查詢各分類最新4條、最熱4條
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context = {'title': '首頁', 'guest_cart': 1,
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type21': type21,
               'type3': type3, 'type31': type31,
               'type4': type4, 'type41': type41,
               'type5': type5, 'type51': type51,}

    return render(request, 'df_goods/index.html', context)

def list(request, tid, pindex, sort):
    tidindb = int(tid) + 1
    typeinfo = TypeInfo.objects.get(pk=tidindb)
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(gtype_id=tidindb).order_by('-id')
    elif sort == '2':
        goods_list = GoodsInfo.objects.filter(gtype_id=tidindb).order_by('-gprice')
    elif sort == '3':
        goods_list = GoodsInfo.objects.filter(gtype_id=tidindb).order_by('-gclick')

    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(pindex))
    context = {'title': typeinfo.ttitle, 'guest_cart': 1,
               'page': page,
               'paginator': paginator,
               'typeinfo': typeinfo,
               'list_id': (int(typeinfo.id) -1),
               'sort': sort,
               'news': news}

    return render(request, 'df_goods/list.html', context)

def detail(request, id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick + 1
    goods.save()

    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]

    context = { 'title': goods.gtype.ttitle, 'guest_cart': 1,
                'g': goods,
                'news': news,
                'id': id}

    response = render(request, 'df_goods/detail.html', context)

    # record the recently views
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_id = '%d'%goods.id

    print('debug:', goods_ids)

    if goods_ids != '':
        goods_ids_list = goods_ids.split(',')
        if goods_ids_list.count(goods_id) >= 1:
            goods_ids_list.remove(goods_id)
        goods_ids_list.insert(0, goods_id)
        print(goods_ids_list)
        if len(goods_ids_list) >= 6:
            del goods_ids_list[5]
        goods_ids = ','.join(goods_ids_list)
    else:
        goods_ids = goods_id

    response.set_cookie('goods_ids', goods_ids)

    return response
