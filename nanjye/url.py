from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index,name="welcome"),
    url(r'^capenyter/$', views.capenter,name="capenter"),

    url(r'^search/', views.search_results, name='search_result'),
    url(r'^article/(\d+)',views.article,name ='article'),
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
