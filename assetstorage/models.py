from django.db import models
from database_storage import DatabaseStorage
from django.conf import settings

class DatabaseStorageWrapper(DatabaseStorage):

    def __init__(self, *args, **kwargs):
        kwargs['options'] = settings.DBS_OPTIONS
        super(DatabaseStorageWrapper, self).__init__(*args, **kwargs)

class Asset(models.Model):
    filename = models.CharField(max_length=255, primary_key=True)
    data = models.TextField()
    size = models.IntegerField()

