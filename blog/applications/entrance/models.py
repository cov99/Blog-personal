# standart library
from datetime import timedelta, datetime
#
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
# Third-party apps
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
# managers
from .managers import EntryManager


class Category(TimeStampedModel):
    """ Categories of an entry """
    short_name = models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True,
    )
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    """ Tags of an article """
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    """ Model for entries or articles """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    tittle = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen',
        upload_to='Entry'
    )
    cover = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
    
    def __str__(self):
        return self.tittle
    
    def get_absolute_url(self):
        return reverse_lazy(
            'entrance_app:entry-detail',
            kwargs={
                'slug': self.slug
            }
        )
    
    def save(self, *args, **kwargs):
        # calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.tittle, str(seconds))

        self.slug = slugify(slug_unique)

        super(Entry, self).save(*args, **kwargs)
