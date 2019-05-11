from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index,name="welcome"),
    url(r'^capenyter/$', views.capenter,name="capenter"),
    url(r'^product/$', views.product,name="product"),
    url(r'^search/', views.search_results, name='search_result'),
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^pay/',views.SavePayment,name ='pay'),
    url(r'^firebase/',views.signin,name ='firebaselogin'),
    url(r'^postsign/',views.postsign,name ='postsign'),
    url(r'^logouts/',views.logout,name ='logout'),
    url(r'^signup/',views.signup,name ='signup'),
    url(r'^postsignup/',views.postsignup,name ='postsignup'),
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
