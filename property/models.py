# -*- coding: utf8 -*-
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator, URLValidator


class Developer(models.Model):
    name = models.CharField(max_length=100)
    reliability = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
                                    blank=True)

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
    line = models.CharField(max_length=50,blank=True)

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
    toilets = models.SmallIntegerField(blank=True)
    toilets_separated = models.BooleanField(blank=True)
    balcony = models.BooleanField(blank=True)
    floor = models.IntegerField(blank=True)
    max_floor = models.IntegerField(blank=True)
    building_type = models.CharField(max_length=2,
                                     choices=BUILDING_TYPE_CHOICES,
                                     blank=True)
    minimal_investment = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    minimal_investment_share = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
                                                 , blank=True)
    reserved_share = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
                                       , blank=True)
    bought_share = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
                                     , blank=True)
    description = models.TextField(blank=True)
    instruction = models.TextField(blank=True)
    contact_name = models.CharField(max_length=50, blank=True)
    developer = models.ForeignKey(Developer, blank=True)
    image = models.ImageField(upload_to='images', default='images/default.jpg')

    def __unicode__(self):
        return self.header + self.address
