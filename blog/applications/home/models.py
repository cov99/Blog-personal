from django.db import models
# Third-party apps
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    """ Model for Home Display Data """
    tittle = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_tittle = models.CharField('Titulo Nosotros', max_length=50)
    abouth_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto',
        null=True,
        blank=True,
    )
    phone = models.CharField('Telefono contacto', max_length=20)

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'
    
    def __str__(self):
        return self.tittle


class Suscribers(TimeStampedModel):
    """ Subscriptions """
    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
    
    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """ Contact form """
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return self.full_name
