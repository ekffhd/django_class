from django.db import models
from django.contrib import admin

from apps.utils import TimeStampedModel


class Board(TimeStampedModel):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)


admin.site.register(Board)
