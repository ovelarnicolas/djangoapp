from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mainApp.models import Usuario, Auto
from django.core.urlresolvers import reverse_lazy
from mainApp.forms import AutoCreateForm


class UsuarioListView(ListView):
    model = Usuario
    object_list = Usuario.objects.all()


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'mainApp/usuario_create.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'mainApp/usuario_update.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'mainApp/usuario_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')


# Ver como implementar
class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoCreateForm
    success_url = reverse_lazy('usuarios_list')

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


def auto_create(request):
    form = AutoCreateForm()
    return render(request, 'mainApp/auto_form_create.html', {'form': form})
