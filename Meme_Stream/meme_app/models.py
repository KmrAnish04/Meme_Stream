from django.db import models

# Create your models here.
class MemeInfo(models.Model):
    nameOfMemeOwner = models.CharField(max_length=50, null=True)
    caption = models.TextField(null=True)
    memeUrl = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameOfMemeOwner
    

    class Meta:
        verbose_name_plural = 'MemeInfo\'s'