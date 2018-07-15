from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import *
from hashlib import sha1
from . import user_decorator
from df_goods.models import *
# Create your views here.

def register(request):
    context = {'title': '用戶註冊'}
    return render(request, 'df_user/register.html', context)


def register_handle(request):
    # get the user register info
    post = request.POST
    uname = post.get('user_name')
    upwd =post.get('pwd')
    ucpwd =post.get('cpwd')
    uemail =post.get('email')

    # comfirm the password
    if upwd != ucpwd:
        return redirect('/user/register/')
    # sha1 hasing
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd_h = s1.hexdigest()

    # create user
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_h
    user.uemail = uemail

    user.save()

    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname = uname).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用戶登錄', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    rememberme = post.get('remember_me', 0)

    # according to the user info
    users = UserInfo.objects.filter(uname = uname) #[]

    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        # hasing the password
        upwd_h = s1.hexdigest()

        if upwd_h == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            redir = HttpResponseRedirect(url)

            if rememberme != 0:
                redir.set_cookie('uname', uname)
            else:
                # set expire time = 0
                redir.set_cookie('uname' '', max_age=-1)

            request.session['user_id'] = users[0].id
            request.session['user_name'] = users[0].uname
            return redir
        else:
            context = {'title': '用戶登錄', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)


    else:
        context = {'title': '用戶登錄', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)


def logout(request):
    red = HttpResponseRedirect('/')
    red.delete_cookie('url')
    request.session.flush()
    return red


@user_decorator.login
def info(request):
    useremail = UserInfo.objects.get(id = request.session['user_id']).uemail

    # recently view
    goods_ids =request.COOKIES.get('goods_ids','')
    goods_ids_list = goods_ids.split(',')
    goods_list = []
    if goods_ids != '':
        for goods_id in goods_ids_list:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {'title': '用戶中心', 'page_name': 1,
               'user_name': request.session['user_name'],
               'user_email': useremail,
               'goods_list': goods_list}
    return render(request, 'df_user/user_center_info.html', context)

@user_decorator.login
def order(request):
    context = {'title': '用戶中心', 'page_name': 1}
    return render(request, 'df_user/user_center_order.html', context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id =request.session['user_id'])

    if request.method == 'POST':
        post = request.POST
        user.ureciever = post.get('receiver')
        user.uaddress = post.get('address')
        user.upostcode = post.get('postcode')
        user.uphone = post.get('phone')
        user.save()

    context = {'title': '用戶中心', 'page_name': 1, 'user': user}
    return render(request, 'df_user/user_center_site.html', context)

