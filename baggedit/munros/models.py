from django.db import models

# Create your models here.

class Munro(models.Model):
    """
    Stores information about a Munro
    """
    NUMBER_OF_MUNROES = 283

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, help_text="The munro's name")
    section = models.ForeignKey('Section', help_text="The section this Munro belongs to")
    translation = models.CharField(max_length=250)
    height = models.IntegerField(help_text="Height in metres")
    summit_grid_ref = models.CharField(max_length=10)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.name

class Section(models.Model):
    """
    Defines a group of Munros e.g. 01 - Loch Lomond to Loch Tay
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return u"%02d - %s" % (self.id, self.name)
