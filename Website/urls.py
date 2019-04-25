
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views 
from django.conf.urls import include, url



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('nanjye.url')),
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
    url(r'^accounts/', include('registration.backends.simple.urls')),
    
   
]
