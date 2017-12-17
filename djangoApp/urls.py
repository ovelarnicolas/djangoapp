"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mainApp.views import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from mainApp import views

urlpatterns = [
    url(r'^$', UsuarioListView.as_view(template_name='static_pages/index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/$', UsuarioListView.as_view(), name='usuarios_list'),
    url(r'^usuario/crear$', UsuarioCreateView.as_view(), name='usuario_create'),
    url(r'^usuario/editar/(?P<pk>\d+)$', UsuarioUpdateView.as_view(), name='usuario_update'),
    url(r'^usuario/borrar/(?P<pk>\d+)$', UsuarioDeleteView.as_view(), name='usuario_delete'),
    url(r'^auto/crear$', views.auto_create, name='auto_crear'),
]
