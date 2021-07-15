from django.db import models
from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    memeData = models.MemeInfo.objects.all()
    # data = []
    for memers in memeData:
        # name = memers.nameOfMemeOwner
        # caption = memers.caption
        # imgUrl = memers.memeUrl
        print(memers.nameOfMemeOwner)
        print(memers.caption)
        print(memers.memeUrl)
        # data.append((name, caption, imgUrl))
    # print(data)
    # stream_data = {
        # 'data': data,
    # }
        
    # print(memeData[2].caption)
    # print(memeData)
    return render(request, 'base.html')

# for streaming the posted memes
def stream(request):
    # memeData = models.MemeInfo.objects.all()
    # print(memeData[2].caption)
    memeData = models.MemeInfo.objects.all()
    data = []
    for memers in memeData:
        name = memers.nameOfMemeOwner
        caption = memers.caption
        imgUrl = memers.memeUrl
        # print(memers.nameOfMemeOwner)
        # print(memers.caption)
        # print(memers.memeUrl)
        data.append((name, caption, imgUrl))
    # print(data)
    stream_data = {
        'data': data,
    }
    print(stream_data['data'])
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



    # memeData = models.MemeInfo.objects.all()
    # print(memeData)

    return render(request, 'meme_app/submitMeme.html')