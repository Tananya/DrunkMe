"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from DrunkMe import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home , name='home'),
    url(r'^detail/(?P<num>[0-9]+)$', views.detail , name='detail'),
    url(r'^menu/(?P<num>[0-9]+)$', views.menu , name='menu'),
    url(r'^searchbar/', views.searchbar , name='searchbar'),
    url(r'^searchdrink/', views.searchdrink , name='searchdrink'),
    url(r'^nearby/', views.nearby , name='nearby'),
    url(r'^promotion/', views.promotion , name='promotion'),
    url(r'^happyhour/', views.happyhour , name='happyhour'),
    url(r'^contents/', views.contents , name='contents'),
    url(r'^areas/', views.areas , name='areas'),
    url(r'^areasdetail/(?P<num>[0-9]+)$', views.areasdetail , name='areasdetail'),
    url(r'^event/', views.event , name='event'),
    url(r'^drinks/', views.drinks , name='drinks'),
    url(r'^eventall/', views.eventall , name='eventall'),
    url(r'^drinkdetail/(?P<category>[\w-]+)$', views.drinkdetail , name='drinkdetail'),
    url(r'^typedrink/(?P<typedrink>[\w-]+)$', views.typedrink , name='typedrink'),
    url(r'^recommended/', views.recommended , name='recommended'),
    url(r'^drinkdst/(?P<num>[0-9]+)$', views.drinkdst , name='drinkdst'),
    url(r'^bar/', views.loginbar , name='loginbar'),
    url(r'^book/', views.book , name='book'),

    url(r'^login/$', auth_views.login, name='login'),# <--
    url(r'^logout/$', auth_views.logout, name='logout'),# <--
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    
]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)