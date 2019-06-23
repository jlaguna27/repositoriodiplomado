from django.contrib import admin  #Por defecto me trae las librerias del administrador
from citas.models import Citamedica, Paciente, Medico, Eps, Profile  #Llamar las tablas de models.py
# Register your models here.

@admin.register(Citamedica)
class Admincitamedica(admin.ModelAdmin):
    list_display = ('id','tipocita', 'estado', 'fecha', 'costo', 'pago', 'nombre_medico', 'nombre_paciente',) #Matriz con registros
    list_filter = ('estado',)

    def nombre_medico(self, medicon): #Función que me muestra el nombre y apellido concatenado
        return "%s %s" % (medicon.medico.user.first_name, medicon.medico.user.last_name)

    def nombre_paciente(self, pacienten):
        return "%s %s" % (pacienten.paciente.user.first_name, pacienten.paciente.user.last_name)


@admin.register(Paciente)
class Adminpaciente(admin.ModelAdmin):
    list_display = ('eps', 'user', 'paciente_nombre',)

    def paciente_nombre(self, pacin):
        return "%s %s" % (pacin.user.first_name, pacin.user.last_name)


@admin.register(Medico)
class Adminmedico(admin.ModelAdmin):
    list_display = ('especialidad', 'user', 'medico_nombre',)

    def medico_nombre(self, medin):
        return "%s %s" % (medin.user.first_name, medin.user.last_name)


@admin.register(Eps)
class Admineps(admin.ModelAdmin):
    list_display = ('eps','regimen','paciente_nombre',)

    def paciente_nombre(self, pacient):
        return "%s %s" % (pacient.paciente.user.first_name, pacient.paciente.user.last_name)


@admin.register(Profile)
class Adminprofile(admin.ModelAdmin):
    list_display = ('genero', 'telefono', 'nacimiento', 'genero', 'user',)
    list_filter = ('genero',)