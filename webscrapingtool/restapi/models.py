from __future__ import unicode_literals
from django.db import models


class Outlet(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Author(models.Model):
    outlet = models.ForeignKey(Outlet, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
