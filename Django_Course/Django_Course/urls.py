"""
URL configuration for Django_Course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Views.index, name='index'),
    path('capitalizefirst', Views.capfirst, name='capfirst'),
    path('removepunc', Views.removepunc, name='rempunc'),
    path('newlineremove', Views.newlineremove, name='newlineremove'),
    path('charcount', Views.charcount, name='charcount'),
    path('spaceremove', Views.spaceremove, name='spaceremove')
    ]
