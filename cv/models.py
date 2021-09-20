from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    descr = models.CharField(max_length=50)
    descr_en = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    descr = models.CharField(max_length=300)
    name_en = models.CharField(max_length=100)
    descr_en = models.CharField(max_length=300)
    stack = models.CharField(max_length=150)
    hasLink = models.BooleanField(default=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    name = models.CharField(max_length=100)
    descr = models.CharField(max_length=300)
    name_en = models.CharField(max_length=100)
    descr_en = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    name = models.CharField(max_length=100)
    descr = models.CharField(max_length=300)
    name_en = models.CharField(max_length=100)
    descr_en = models.CharField(max_length=300)
    time = models.CharField(max_length=100)
    time_en = models.CharField(max_length=100, default="-")

    def __str__(self):
        return self.name
