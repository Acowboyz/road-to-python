from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myexp', views.myExp),
    url(r'^uploadpic$', views.uploadpic),
    url(r'^uploadhandle$', views.uploadhandle),
    url(r'^herolist/(\d*)[/]?$', views.herolist),
    url(r'^area/$', views.area),
    url(r'^area/(\d+)/$', views.area2),
    url(r'htmleditor/', views.htmleditor),
    url(r'htmleditorhandle/', views.htmleditorhandle),
    url(r'^cache1/', views.cache1),
    url(r'^cache2/', views.cache2),
    url(r'^mysearch/',views.mysearch),
    url(r'^celerytest/', views.celerytest)
]