from django.conf.urls import include, url
from . import views, views1

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$', views.detail, name='detail'),

    url(r'^gettest1/$', views.gettest1),
    url(r'^gettest2/$', views.gettest2),
    url(r'^gettest3/$', views.gettest3),

    url(r'^posttest1/$', views.posttest1),
    url(r'^posttest2/$', views.posttest2),

    url(r'^cookietest/$', views.cookietest),

    url(r'^redirecttest1/', views.redirecttest1),
    url(r'^redirecttest2/', views.redirecttest2),

    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3),


]
