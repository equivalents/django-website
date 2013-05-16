from django.db import models
from django.contrib.auth.models import User


class Pin(models.Model):
  pinID = models.PositiveSmallIntegerField()
  pinNumber = models.PositiveSmallIntegerField()
  pinDirection = models.CharField(max_length=3)
  pinStatus = models.CharField(max_length=6)
  pinDescription = models.CharField(max_length=6)
  pinUpdate = models.BooleanField()
  #user = models.ForeignKey(User)
  def __str__(self):
    return '%s, %s' % (self.pinDescription, self.pinDirection)

class Slider(models.Model):
  sliderID = models.PositiveSmallIntegerField()
  sliderNumber = models.PositiveSmallIntegerField()
  sliderDescription = models.CharField(max_length=6)
  sliderValue = models.PositiveIntegerField()
  sliderUpdate = models.BooleanField()
  #user = models.ForeignKey(User)
  def __str__(self):
    return '%s, %s' % (self.sliderDescription, self.sliderValue)
	
class Preprogram(models.Model):
  preprogramID = models.PositiveSmallIntegerField()
  preprogramNumber = models.PositiveSmallIntegerField()
  preprogramDirection = models.CharField(max_length=3)
  preprogramStatus = models.CharField(max_length=6)
  preprogramDescription = models.CharField(max_length=6)
  preprogramValue = models.PositiveIntegerField()
  preprogramUpdate = models.BooleanField()
  #user = models.ForeignKey(User)
  def __str__(self):
    return '%s, %s, %s' % (self.preprogramDescription, self.preprogramStatus, self.preprogramValue)