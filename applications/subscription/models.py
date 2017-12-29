from django.db import models
from oscar.apps.dashboard.catalogue.models import *  # noqa isort:skip

class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email