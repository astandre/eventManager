from django.db import models


# TODO cambiar los tamaños de los campos
# Create your models here.
class Local(models.Model):
    cod_local = models.AutoField(primary_key=True)
    nombre_local = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    direccion_local = models.CharField(max_length=200)
    latitud_local = models.CharField(max_length=200, default="0")
    longitud_local = models.CharField(max_length=200, default="0")
    nombre_propietario = models.CharField(max_length=60)
    telefono_local = models.CharField(max_length=15)
    celular_local = models.CharField(max_length=12)
    email_local = models.EmailField()
    img_local = models.CharField(max_length=300, default="img.png")

    class Meta:
        default_related_name = 'Local'
        verbose_name_plural = "Locales"
        verbose_name = "Local"

    def __str__(self):
        return self.nombre_local


# class CatEvento(models.Model):
#
#     # nombre_categoria = models.CharField(max_length=20)
#
#     class Meta:
#         default_related_name = 'CatEvento'
#         verbose_name_plural = "CatEventos"
#         verbose_name = "CatEvento"
#
#     def __str__(self):
#         return self.nombre_categoria
#     # def is_upperclass(self):
#     #     return  self.nombre_categoria in (self.CATEGORIAS_CHOICES.FARRA)


class Evento(models.Model):
    MUSICA = 'M'
    TEATRO = 'T'
    GAMING = 'G'
    POLITICA = 'P'
    DEPORTES = 'D'
    FARRA = 'F'

    CATEGORIAS_CHOICES = (
        (MUSICA, 'Musica'),
        (TEATRO, 'Teatro'),
        (GAMING, 'Gaming'),
        (POLITICA, 'Politica'),
        (DEPORTES, 'Deportes'),
        (FARRA, 'Farra')
    )
    cod_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=30)
    descripcion_evento = models.TextField()
    activo = models.BooleanField(default=True)
    familiar = models.BooleanField(default=True)
    direccion_evento = models.CharField(max_length=60)
    latitud_evento = models.CharField(max_length=15, default="-3.984197")
    longitud_evento = models.CharField(max_length=15, default="-79.200370")
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    img = models.CharField(max_length=300)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    nombre_categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS_CHOICES,
        default=FARRA
    )

    class Meta:
        default_related_name = 'Evento'
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"

    def __str__(self):
        return self.nombre_evento

# class CalificacionEvento(models.Model):
#     cod_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
#     Calif_Choices =('0','1','2','3','4','5')
#     calif_evento = models.CharField( max_length=1,
#                                      choices=Calif_Choices,
#                                      default='0')
