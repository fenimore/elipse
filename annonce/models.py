from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone

#Random id generator
def pkgen():
    from hashlib import sha1
    from random import random
    pk = sha1(str(random()).encode('utf-8')).hexdigest().lower()[:6]
    return pk


class Donne(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField('pub date')
    myzip = models.IntegerField()
    location = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pics', null=True)
    status = models.BooleanField(default=True)
    quality = models.CharField(max_length=9)
    mytype = models.CharField(max_length=10)
    user = models.ForeignKey(User)
    pseudo_email = models.CharField(max_length=50)
    
    def _str__(self):
        return self.title

class Pret(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    myzip = models.IntegerField()
    location = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pics', null=True)
    status = models.BooleanField(default=True)
    quality = models.CharField(max_length=9)
    mytype = models.CharField(max_length=10)
    user = models.ForeignKey(User)
    pseudo_email = models.CharField(max_length=50)
    
    def _str__(self):
        return self.title
    
class Exchice(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    myzip = models.IntegerField()
    location = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pics', null=True)
    status = models.BooleanField(default=True)
    quality = models.CharField(max_length=9)
    duration = models.CharField(max_length=9)
    mytype = models.CharField(max_length=10)
    user = models.ForeignKey(User)
    pseudo_email = models.CharField(max_length=50)
    
    def _str__(self):
        return self.title
