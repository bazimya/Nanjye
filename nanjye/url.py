from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index,name="welcome"),
    url(r'^smartphone/',views.smartphone,name="smartphone"),
    url(r'^details/(?P<userid>\d+)/$',views.contact,name="contact"),
    url(r'^contact/',views.contact,name="contact"),
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
