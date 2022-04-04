from django.db import models

# Create your models here.
class City(models.Model):

    name = models.CharField(max_length=35)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name
