from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile (models.Model):
    Genero=((1,"M"),
            (2,"F"),
            (3,"O"),)
    documento=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    nacimiento=models.DateField()
    genero=models.SmallIntegerField(choices=Genero)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='profile'


class Eps(models.Model):
    Regimen=((1,"Contributivo"),
             (2,"Subsidiado"),)
    eps=models.CharField(max_length=50)
    regimen=models.SmallIntegerField(choices=Regimen)

    class Meta:
        db_table='eps'

    def __str__(self):
        return self.eps


class Paciente(models.Model):
    eps=models.OneToOneField(Eps, on_delete=models.PROTECT)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='paciente'

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Medico(models.Model):
    especialidad=models.CharField(max_length=50)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='medico'

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Citamedica(models.Model):
    Estado=((1,"Aprobada"),
            (2,"Rechadaza"),
            (3,"Ejecutada"),)
    Pago=((2,"Pago"),
          (3,"No pago"),)
    tipocita=models.CharField(max_length=50)
    estado=models.SmallIntegerField(choices=Estado)
    fecha=models.DateField()
    costo=models.CharField(max_length=10)
    pago=models.SmallIntegerField(choices=Pago)
    medico=models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente=models.ForeignKey(Paciente, on_delete=models.PROTECT)

    class Meta:
        db_table='citamedica'