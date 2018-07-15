from django.shortcuts import render, redirect
from django.http import JsonResponse
from df_user import user_decorator
from .models import *

# Create your views here.

@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(cuser_id=uid)
    count = carts.count()
    context = { 'title': '購物車', 'page_name': 1,
                'carts': carts,
                'count': count
    }
    return render(request, 'df_cart/cart.html', context)

@user_decorator.login
def add(request, gid, count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)

    carts = CartInfo.objects.filter(cuser_id=uid, cgoods_id=gid)

    if len(carts) >= 1:
        cart = carts[0]
        cart.ccount = cart.ccount + count
    else:
        cart = CartInfo()
        cart.cuser_id = uid
        cart.cgoods_id = gid
        cart.ccount = count
    cart.save()

    # response = redirect('/cart/')
    # res

    if request.is_ajax():
        count = CartInfo.objects.filter(cuser_id=request.session['user_id']).count()
        return JsonResponse({'count': count})
    else:
        return redirect('/cart/')


@user_decorator.login
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.ccount = int(count)
        cart.save()
        data={'ok': 0}
    except Exception:
        data = {'ok': count1}

    return JsonResponse(data)

@user_decorator.login
def delete(request, cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok': 1}
    except Exception:
        data = {'ok': 0}

    return JsonResponse(data)
