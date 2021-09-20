from django.db import models

SHORT_FIELD = 100
DESCRIPTION_LENGTH = 600


class Skill(models.Model):
    """
    Languages, frameworks, libraries and tools
    """
    TYPE_CHOICES = [
        ('backend', 'backend'),
        ('frontend', 'frontend'),
        ('ds', 'ds'),
        ('General', 'General')
    ]

    name = models.CharField(max_length=SHORT_FIELD)
    type = models.CharField(max_length=SHORT_FIELD, choices=TYPE_CHOICES)
    descr = models.CharField(max_length=SHORT_FIELD)
    descr_en = models.CharField(max_length=SHORT_FIELD)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Free time projects
    """
    name = models.CharField(max_length=SHORT_FIELD)
    descr = models.CharField(max_length=DESCRIPTION_LENGTH)
    name_en = models.CharField(max_length=SHORT_FIELD)
    descr_en = models.CharField(max_length=DESCRIPTION_LENGTH)
    stack = models.CharField(max_length=DESCRIPTION_LENGTH)
    hasLink = models.BooleanField(default=True)
    link = models.CharField(max_length=SHORT_FIELD, blank=True, null=True)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    """
    Soft skills
    """
    name = models.CharField(max_length=SHORT_FIELD)
    descr = models.CharField(max_length=DESCRIPTION_LENGTH)
    name_en = models.CharField(max_length=SHORT_FIELD)
    descr_en = models.CharField(max_length=DESCRIPTION_LENGTH)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    """
    Places of works, positions in them and experiences gained
    """
    name = models.CharField(max_length=SHORT_FIELD)
    descr = models.CharField(max_length=DESCRIPTION_LENGTH)
    name_en = models.CharField(max_length=SHORT_FIELD)
    descr_en = models.CharField(max_length=DESCRIPTION_LENGTH)
    stack = models.CharField(max_length=DESCRIPTION_LENGTH, null=True)
    time = models.CharField(max_length=SHORT_FIELD)
    time_en = models.CharField(max_length=SHORT_FIELD, null=True)

    def __str__(self):
        return self.name
