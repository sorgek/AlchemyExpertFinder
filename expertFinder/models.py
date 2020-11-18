from django.db import models
from django.forms import ModelForm
from django.views.generic import ListView


# the great expert finder model!
class Expert(models.Model):
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    avatar = models.ImageField(upload_to='images/')
    organization = models.CharField(max_length=100)
    techSkills = models.TextField()
    courseWork = models.TextField()
    gitRepo = models.URLField()
    linkedIn = models.URLField()
    twitter = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.lastName




