from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Citamedica
from .forms import Formulariocita

class Viendocitas(PermissionRequiredMixin, ListView):
    permission_required = 'citas.view_citamedica'
    login_url = 'login'
    model = Citamedica
    template_name = 'vercita.html'

    def get_queryset(self):
        queryset = super(Viendocitas, self).get_queryset()

        if self.request.user.groups.filter(name="Pacientes").exists():
            queryset = queryset.filter(paciente__user=self.request.user)

        if self.request.user.groups.filter(name="Medicos").exists():
            queryset = queryset.filter(medico__user=self.request.user)

        return queryset


class Insertarcita(PermissionRequiredMixin, FormView):
    permission_required = 'citas.add_citamedica'
    login_url = 'login'
    form_class = Formulariocita
    template_name = 'insertarcita.html'
    success_url = '/vercita'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Editcita(PermissionRequiredMixin, UpdateView):
    permission_required = 'citas.change_citamedica'
    login_url = 'login'
    model = Citamedica
    form_class = Formulariocita
    template_name = 'editcita.html'
    success_url = '/vercita'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elicita(PermissionRequiredMixin, DeleteView):
    permission_required = 'citas.del_citamedica'
    login_url = 'login'
    model = Citamedica
    template_name = 'elicita.html'
    success_url = '/vercita'
