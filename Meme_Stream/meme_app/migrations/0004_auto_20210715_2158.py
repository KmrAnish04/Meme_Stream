# Generated by Django 3.1.6 on 2021-07-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme_app', '0003_auto_20210715_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memeinfo',
            name='caption',
            field=models.TextField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='memeinfo',
            name='memeUrl',
            field=models.TextField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='memeinfo',
            name='nameOfMemeOwner',
            field=models.CharField(default='no name', max_length=50),
        ),
    ]
