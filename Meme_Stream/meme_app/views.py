from django.db import models
from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, 'base.html')


def openForm(request):
    memeData = models.MemeInfo.objects.all()
    print(memeData[2].caption)
    return render(request, 'meme_app/submitMeme.html')

def submitMeme(request):
    memerName = request.POST.get('memerName')
    caption = request.POST.get('caption')
    memeURL = request.POST.get('memeURL')
    # print(memerName, caption, memeURL)

    models.MemeInfo.objects.create(nameOfMemeOwner=memerName, caption=caption, memeUrl=memeURL)
    # memeData = models.MemeInfo.objects.all()
    # print(memeData)

    return render(request, 'meme_app/submitMeme.html')