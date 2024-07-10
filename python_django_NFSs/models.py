from django.db import models

# Create your models here.
class ModelWithFileField(models.Model):
    path = models.FileField(upload_to=".")