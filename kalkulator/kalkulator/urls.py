"""kalkulator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('but1',but1,name="but1"),
    path('but_plus',but_plus,name="but_plus"),
    path('equale',equale,name="equale"),
    path('erase',erase,name="erase"),
    path('but2',but2,name="but2"),
    path('but3',but3,name="but3"),
    path('but4',but4,name="but4"),
    path('but5',but5,name="but5"),
    path('but6',but6,name="but6"),
    path('but7',but7,name="but7"),
    path('but8',but8,name="but8"),
    path('but9',but9,name="but9"),
    path('but0',but0,name="but0"),
    path('ONAV',ONAV,name="ONAV"),
    path('CNAV',CNAV,name="CNAV"),
    path('but_minus',but_minus,name="but_minus"),
    path('but_multi',but_multi,name="but_multi"),
    path('but_t',but_t,name="but_t")

]
