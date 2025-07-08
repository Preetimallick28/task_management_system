from django.db import models

# Create your models here.
class add(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

class HistoryModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

class CompleteModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

