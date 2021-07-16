from django.db import models
from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    memeData = models.MemeInfo.objects.all()
    date = models.MemeInfo.objects.order_by('-created')
    # a = models.MemeInfo.objects.get(id=29)
    print(date)

    return render(request, 'base.html')

def openEditForm(request):
    return render(request, 'meme_app/editMeme.html')


# for streaming the posted memes
def stream(request):
    memeData = models.MemeInfo.objects.order_by('-created')
    data = []
    for memers in memeData:
        name = memers.nameOfMemeOwner
        caption = memers.caption
        imgUrl = memers.memeUrl
        memeId = memers.id
        print(memers.id)
        data.append((name, caption, imgUrl, memeId))
    # print(data)
    stream_data = {
        'data': data,
    }
    # print(stream_data['data'])
    return render(request, 'meme_app/streamPage.html', stream_data)

# Only for opening the submit form
def openForm(request):
    return render(request, 'meme_app/submitMeme.html')

def submitMeme(request):
    memerName = request.POST.get('memerName')
    caption = request.POST.get('caption')
    memeURL = request.POST.get('memeURL')
    # print(memerName, caption, memeURL)

    if request.POST.get('memerName') and request.POST.get('memeURL'):
        models.MemeInfo.objects.create(nameOfMemeOwner=memerName, caption=caption, memeUrl=memeURL)
    # models.MemeInfo.objects.create(nameOfMemeOwner=memerName, caption=caption, memeUrl=memeURL)



    # memeData = models.MemeInfo.objects.all()
    # print(memeData)

    return render(request, 'meme_app/submitMeme.html')

def editMeme(request):
    return render(request, 'meme_app/streamPage.html')