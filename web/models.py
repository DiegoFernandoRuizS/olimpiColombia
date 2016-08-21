from django.db import models
from django.contrib.auth.models import User


class Sport(models.Model):
    name = models.CharField(max_length=200, null=False)
    icon = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Athlete(models.Model):
    identification = models.CharField(max_length=11)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20)
    birth_place = models.CharField(max_length=50, null=False)
    birthdate = models.DateField()
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    coach_name = models.CharField(max_length=50)
    # Campo del video
    link_video = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, null=False)
    highlight = models.CharField(max_length=70, null=True)
    photo = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.first_name + ' ' +  self.last_name

    class Meta:
        ordering = ['last_name']

class ScheduleItem(models.Model):
    datetime = models.DateTimeField(null=False)
    # PROGRAMADO, EN CURSO o FINALIZADO
    state = models.CharField(max_length=20, null=False)
    result = models.CharField(max_length=20)
    modality = models.CharField(max_length=20)
    sport = models.ForeignKey(Sport, null=False)
    athlete = models.ForeignKey(Athlete, null=False)

    def __str__(self):
        return self.state


class VisitRegistry(models.Model):
    user_app = models.ForeignKey(User, null=True)
    user_fb = models.CharField(max_length=25)
    datetime = models.DateTimeField(null=False)
    ip = models.CharField(max_length=15)
    # Usuario Registrado en el Sistema o Usuario de Redes Sociales
    user_type = models.CharField(max_length=15)
    """ Permite identificar los atletas mas populares,
    teniendo en cuenta las visitas a su perfil
    """
    athlete = models.ForeignKey(Athlete, null=False)

    def __str__(self):
        return self.ip
