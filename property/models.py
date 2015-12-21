# -*- coding: utf8 -*-
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator, URLValidator


class Developer(models.Model):
    name = models.CharField(max_length=100)
    reliability = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
                                    null=True, blank=True)

    def __unicode__(self):
        return self.name


class Regions(models.Model):
    """ Regions model """
    parent_id = models.IntegerField()
    type = models.SmallIntegerField()
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class MetroStations(models.Model):
    name = models.CharField(max_length=50)
    line = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name



class Property(models.Model):
    """Property object"""
    PROPERTY_TYPE_CHOICES = (
        ('FL', 'Квартира'),
        ('PH', 'Пентхаус'),
        ('TH', 'Таунхаус'),
        ('CH', 'Загородные дома'),
    )
    BUILDING_TYPE_CHOICES = (
        ('PA', 'Панельный'),
        ('MO', 'Монолитный'),
        ('BR', 'Кирпичный'),
        ('BL', 'Блочный'),
        ('MB', 'Монолитно-кирпичный'),
    )
    property_type = models.CharField(max_length=2,
                                     choices=PROPERTY_TYPE_CHOICES)
    address = models.CharField(max_length=300)
    header = models.CharField(max_length=100)
    region = models.ForeignKey(Regions)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    meters = models.DecimalField(max_digits=5, decimal_places=2)
    toilets = models.SmallIntegerField(null=True, blank=True)
    toilets_separated = models.NullBooleanField()
    balcony = models.NullBooleanField()
    floor = models.IntegerField(null=True, blank=True)
    max_floor = models.IntegerField(null=True, blank=True)
    building_type = models.CharField(max_length=2,
                                     choices=BUILDING_TYPE_CHOICES,
                                     null=True,
                                     blank=True)
    minimal_investment = models.DecimalField(max_digits=20,
                                             decimal_places=2,
                                             null=True,
                                             blank=True)
    minimal_investment_share = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
                                                 , null=True
                                                 , blank=True)
    reserved_share = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
                                       , null=True
                                       , blank=True)
    bought_share = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
                                     , null=True
                                     , blank=True)
    description = models.TextField(null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    developer = models.ForeignKey(Developer, null=True, blank=True)
    image = models.ImageField(upload_to='images', default='images/default.jpg')

    def __unicode__(self):
        return self.header + " " + self.address
