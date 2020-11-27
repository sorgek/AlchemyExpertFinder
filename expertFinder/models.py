from django.db import models
from django.forms import ModelForm
from django.views.generic import ListView
from django.urls import reverse

# the great expert finder model!
class Expert(models.Model):
    firstName = models.CharField("First Name", max_length=55)
    lastName = models.CharField("Last Name", max_length=55)
    avatar = models.ImageField(upload_to='images/')
    organization = models.CharField(max_length=100)
    techSkills = models.TextField("Tech Skills")
    courseWork = models.TextField("OSU Course Work")
    gitRepo = models.URLField("Git Repo")
    linkedIn = models.URLField()
    twitter = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.lastName

    def get_absolute_url(self):
        return reverse('expertFinder:display_expert', args=[self.id])



