from django.db import models

# Create your models here.
class TextFile(models.Model):
    text_name = models.CharField(max_length=50)
    text_text = models.CharField(max_length=1000)
    text_modify_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_name