from django.conf.urls import url
from mainApp.views import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from mainApp import views

urlpatterns = [
    url(r'^/$', UsuarioListView.as_view(), name='usuarios_list'),
    url(r'^/crear$', UsuarioCreateView.as_view(), name='usuario_create'),
    url(r'^/editar/(?P<pk>\d+)$', UsuarioUpdateView.as_view(), name='usuario_update'),
    url(r'^/borrar/(?P<pk>\d+)$', UsuarioDeleteView.as_view(), name='usuario_delete'),    
]