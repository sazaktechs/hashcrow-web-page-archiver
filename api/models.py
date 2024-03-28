''' 
Models

A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; 
see Making queries. 
'''

#from django.conf import settings
from django.db import models
from django.utils import timezone

class Url(models.Model):
    ''' Url Object '''
    
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=200, primary_key=True)
    str_url = str(url)
    
    def __str__(self):
        return self.str_url

class Hash(models.Model):
    ''' Hash Object '''
    hash = models.CharField(max_length=200)
    str_hash = str(hash)
    
    url = models.ForeignKey(Url, related_name="snapshots", on_delete=models.CASCADE)

    def __str__(self):
        return self.str_hash

class SnapShot(models.Model):
    ''' SnapShot Object '''

    hash = models.ForeignKey(Hash, related_name='content', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    # html = models.TextField()

    str_created_date = str(created_date)

    def __str__(self):
        return self.str_created_date