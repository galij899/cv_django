from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    level = models.IntegerField()
    descr = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    descr = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class SoftSkill(models.Model):
    name = models.CharField(max_length=50)
    descr = models.CharField(max_length=300)

    def __str__(self):
        return self.name
