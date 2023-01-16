from django.db import models
from django.conf import settings
# Third-party apps
from model_utils.models import TimeStampedModel
#
from applications.entrance.models import Entry
# managers
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """ Model for favorites """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Favorite Post'
        verbose_name_plural = 'Favorite Posts'
    
    def __str__(self):
        return self.entry.tittle
