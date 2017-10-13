# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

class UserManager(models.Manager):
    
    def create_user(self, name, password):
        user = self.create(name=name, password=password)
        user.dateAdded = datetime.datetime.now()
        return user

class User(models.Model):
    objects = UserManager()
    
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    dateAdded = models.DateTimeField('date added')
    profile_id =  models.CharField(max_length=25)
    
    def add_profile(self, profile):
        profile.user = self.profile_id
        


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=25)
    details = models.CharField(max_length=250)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        print('Cowabunga, Dude!')
        return True

    def active(self):
        if self.user is not None:
            return True
        else: 
            return False 
        
            