from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
	
   class Meta:
        verbose_name = _('card')
        verbose_name_plural = _('cards')
        ordering = ('-created_at', )

    def __str__(self):
        return '{} (#{})'.format(self.title, self.pk)