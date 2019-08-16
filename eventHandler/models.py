from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# TODO cambiar los tamaños de los campos
# Create your models here.


class Direccion(models.Model):
    calle_principal = models.CharField(max_length=100)
    calle_secundaria = models.CharField(max_length=100)
    refencia = models.CharField(max_length=100)
    latitud = models.CharField(max_length=15, default="-3.984197")
    longitud = models.CharField(max_length=15, default="-79.200370")

    class Meta:
        default_related_name = 'direccion'
        verbose_name_plural = "Direcciones"
        verbose_name = "Direccion"

    def __str__(self):
        return "%s, %s Ref: %s" % (self.calle_principal, self.calle_secundaria, self.refencia)


class CalificacionManager(models.Manager):
    # TODO add real method that returns current calificacion
    def get_calificacion(self):
        return 5


class Local(models.Model):
    id_local = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    nombre_propietario = models.CharField(max_length=60)
    telefono = PhoneNumberField(blank=True)
    celular = PhoneNumberField(blank=True)
    email = models.EmailField()
    image = models.CharField(max_length=300, default="img.png")

    # objects = CalificacionManager()

    class Meta:
        default_related_name = 'local'
        verbose_name_plural = "Locales"
        verbose_name = "Local"

    def __str__(self):
        return self.nombre


class EventoQuerySet(models.QuerySet):
    def musica(self):
        return self.filter(categoria=Evento.MUSICA, activo=True)

    def teatro(self):
        return self.filter(categoria=Evento.TEATRO, activo=True)

    def gaming(self):
        return self.filter(categoria=Evento.GAMING, activo=True)

    def politica(self):
        return self.filter(categoria=Evento.POLITICA, activo=True)

    def deportes(self):
        return self.filter(categoria=Evento.DEPORTES, activo=True)

    def fiesta(self):
        return self.filter(categoria=Evento.FIESTA, activo=True)


class EventoManager(models.Manager):
    def get_queryset(self):
        return EventoQuerySet(self.model, using=self._db)

    def musica(self):
        return self.get_queryset().musica()

    def teatro(self):
        return self.get_queryset().teatro()

    def gaming(self):
        return self.get_queryset().gaming()

    def politica(self):
        return self.get_queryset().politica()

    def deportes(self):
        return self.get_queryset().deportes()

    def fiesta(self):
        return self.get_queryset().fiesta()


class Evento(models.Model):
    MUSICA = 'M'
    TEATRO = 'T'
    GAMING = 'G'
    POLITICA = 'P'
    DEPORTES = 'D'
    FIESTA = 'F'
    CATEGORIAS = (MUSICA, TEATRO, GAMING, POLITICA, DEPORTES, FIESTA)
    CATEGORIAS_CHOICES = (
        (MUSICA, 'Musica'),
        (TEATRO, 'Teatro'),
        (GAMING, 'Gaming'),
        (POLITICA, 'Politica'),
        (DEPORTES, 'Deportes'),
        (FIESTA, 'Fiesta')
    )
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    familiar = models.BooleanField(default=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    image = models.CharField(max_length=300, default="img.png")
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS_CHOICES,
        default=FIESTA
    )
    objects = EventoManager()

    class Meta:
        default_related_name = 'evento'
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    ZERO = 0
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5

    CALIF_CHOICES = (
        (ZERO, '0'),
        (VERY_LOW, '1'),
        (LOW, '2'),
        (MEDIUM, '3'),
        (HIGH, '4'),
        (VERY_HIGH, '5')
    )
    calificacion = models.IntegerField(choices=CALIF_CHOICES, default=0)
    comentario = models.CharField(max_length=20, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)

    #    TODO Asking to user
    class Meta:
        default_related_name = 'calificacion'
        verbose_name_plural = "Calificaciones"
        verbose_name = "Calificacion"

    def __str__(self):
        return self.comentario
