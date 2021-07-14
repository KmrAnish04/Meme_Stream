from django.db import models

# Create your models here.
class MemeInfo(models.Model):
    nameOfMemeOwner = models.CharField(max_length=50)
    caption = models.TextField()
    memeUrl = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Meme_Information
    class Meta:
        verbose_name_plural = 'Memes_Informations'