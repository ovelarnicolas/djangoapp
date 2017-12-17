from django.conf.urls import url
from mainApp.views import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from mainApp import views

urlpatterns = [
    url(r'^$', UsuarioListView.as_view(), name='usuarios_list'),
    url(r'^new$', UsuarioCreateView.as_view(), name='usuario_create'),
    url(r'^edit/(?P<pk>\d+)$', UsuarioUpdateView.as_view(), name='usuario_update'),
    url(r'^delete/(?P<pk>\d+)$', UsuarioDeleteView.as_view(), name='usuario_delete'),    
]