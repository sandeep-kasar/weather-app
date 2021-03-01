from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
