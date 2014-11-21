from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Ciclo(models.Model):
    clave = models.CharField(max_length=10)
    fecha_revision = models.DateField()
    observacion = models.TextField(null=True, default='', blank=True)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Ciclo ' + self.clave


class Dimension(models.Model):
    dimension = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Dimensiones'

    def __unicode__(self):
        return self.dimension


class Objetivo(models.Model):
    dimension = models.ForeignKey(Dimension)
    ciclo = models.CharField(max_length=10)
    objetivo = models.TextField()

    def __unicode__(self):
        return self.objetivo


class Perfil(models.Model):
    usuario = models.ForeignKey(User, unique=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __unicode__(self):
        return self.usuario.username


class Proyecto(models.Model):
    lider = models.ForeignKey(User, null=True, blank=True)
    perfil = models.ForeignKey(Perfil, null=True, blank=True)
    dimension = models.ForeignKey(Dimension)
    objetivo = models.ForeignKey(Objetivo)
    titulo = models.TextField()
    fecha_plazo = models.DateField()
    revision = models.FloatField(default=0, null=True, blank=True)
    cumplimiento = models.FloatField(default=0)
    indicador = models.CharField(max_length=50, null=True, default='', blank=True)
    adjunto = models.FileField(upload_to='documentos', null=True, blank=True)
    abierto = models.FloatField(blank=True, null=True, default=0)
    cerrado = models.FloatField(blank=True, null=True, default=0)
    observacion_revision = models.TextField(default='', null=True, blank=True)
    actualizado = models.BooleanField(default=False)
    revisado = models.BooleanField(default=False)
    fecha_revision = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['cumplimiento']

    def save(self):
        super(Proyecto, self).save()
        if self.cumplimiento >= 100:
            self.cerrado = 1
            self.abierto = 0
        else:
            self.cerrado = 0
            self.abierto = 1
        super(Proyecto, self).save()

    def semaforo(self):
        if self.cerrado == 1:
            return 'blue'
        else:
            if self.fecha_plazo < date.today():
                return 'red'
            elif self.fecha_plazo.strftime('%m') == date.today().strftime('%m'):
                return 'orange'
            else:
                return 'green'

    def __unicode__(self):
        return self.titulo


class Observacion(models.Model):
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True)
    observacion = models.CharField(max_length=10000)
    usuario = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Observaciones'

    def __unicode__(self):
        return self.observacion


class Avance(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    ciclo = models.ForeignKey(Ciclo)
    avance = models.FloatField(default=0)
    checkeado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.proyecto.titulo

class Revisiones(models.Model):
    proyecto = models.ForeignKey(Proyecto, null=True)
    cumplimiento = models.FloatField(default=0)
    observacion = models.TextField()
    actualizado = models.BooleanField(default=False)
    revisado = models.BooleanField(default=False)
