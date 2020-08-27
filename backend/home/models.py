from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Sample(models.Model):
    "Generated Model"
    address1 = models.CharField(max_length=256,)
    address2 = models.CharField(max_length=256,)
    city = models.CharField(max_length=256,)
    state = models.CharField(max_length=5,)
    zip = models.IntegerField()
    date = models.DateField()
