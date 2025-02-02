from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.


class Place(models.Model):
  title = models.CharField(max_length=200, verbose_name='Название места')
  description_short = models.TextField(verbose_name='Краткое описание')
  description_long = HTMLField(verbose_name='Полное описание')
  longitude = models.FloatField(verbose_name='Долгота')
  latitude = models.FloatField(verbose_name='Широта')

  def __str__(self):
    return self.title


class Image(models.Model):
  ordinal_number = models.PositiveIntegerField(
    verbose_name='Порядок картинки',
    default=0,
    blank=False,
    null=False,
    db_index=True
  )

  image = models.ImageField(verbose_name='Картинка')
  place = models.ForeignKey(
    Place,
    on_delete=models.CASCADE,
    related_name='images',
    verbose_name='Интересное место'
  )

  class Meta:
    ordering = ['ordinal_number']

  def image_preview(self):
    if self.image:
      return format_html(
        '<img src="{}" style="max-width: 255px; max-height: 200px;" />',
        self.image.url
      )
    return ''

  def __str__(self):
    return f'{self.ordinal_number} {self.place.title}'
