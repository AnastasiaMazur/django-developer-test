from django.db import models
from django.contrib.auth.models import User


class Step(models.Model):
    name = models.CharField(max_length=100)
    explanation = models.TextField(max_length=500)

    def __unicode__(self):
        return "{}:{}".format(self.name, self.explanation)


class Roadmap(models.Model):
    name = models.CharField(max_length=100)
    publications = models.ManyToManyField(Step)

    def __unicode__(self):
        return "{}".format(self.name)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, related_name="owner")
    roadmap = models.ForeignKey(Roadmap, related_name="project")

    def __unicode__(self):
        return "ID:{}, {}".format(self.id, self.name)
