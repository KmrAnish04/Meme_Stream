from django.db import models

# Create your models here.
class MemeInfo(models.Model):
    nameOfMemeOwner = models.CharField(max_length=50, null=False, default='no name')
    caption = models.TextField(null=False, default='N/A')
    memeUrl = models.TextField(null=False, default='N/A')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameOfMemeOwner
    

    class Meta:
        verbose_name_plural = 'MemeInfo\'s'