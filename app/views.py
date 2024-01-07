from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.


def insert_topic(request):
    ETFO = Topicform()
    d={'ETFO':ETFO}
    if request.method == 'POST':
        TDO = Topicform(request.POST)
        if TDO.is_valid():
            TDO.save()
            QLTO = Topic.objects.all()
            dic={'topics':QLTO}
            return render(request,'display_topic.html',dic)
        else:
            return HttpResponse('<center> invalid data')


    return render(request,'insert_topic.html',d)







def insert_webpage(request):
    EWFO = Webpageform()
    d2={'EWFO':EWFO}
    if request.method == 'POST':
        WDO = Webpageform(request.POST)
        if WDO.is_valid():
            WDO.save()
            WO = Webpage.objects.all()
            dic={'webpage':WO}
            return render(request,'display_webpage.html',dic)
        else:
            return HttpResponse('<center> invalid data')


    return render(request,'insert_webpage.html',d2)







def insert_acessrecord(request):
    EAFO = Acessrecordform()
    d3={'EAFO':EAFO}
    if request.method == 'POST':
        FAD = Acessrecordform(request.POST)
        if FAD.is_valid():
            FAD.save()
            AO = Acessrecord.objects.all()
            dic = {'ar':AO}
            return render(request,'display_acessrecord.html',dic)
        
        else:
            return HttpResponse('<center> invalid data')



    return render(request,'insert_acessrecord.html',d3)