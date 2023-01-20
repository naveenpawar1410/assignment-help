from django.shortcuts import render
from help.models import contectus
from help.models import bloge

def contectus1(request):
    if(request.method=='POST'):
        m=contectus()
        m.name=request.POST['name']
        m.email=request.POST['email']
        m.contact=request.POST['num']
        m.subject=request.POST['subject']
        m.discription=request.POST['desc']
        m.budget=request.POST['budget']

        m.save()
        # data=contectus.objects.all()
        return render(request,"contectus.html")
    return render(request,"contectus.html")  


def viewAll(request):
    data=contectus.objects.all()
    return render(request,"aspage.html",{'myrecord':data}) 

def login(request):
    return render(request,"login.html") 

def bloge1(request):
    if(request.method=='POST'):
        a=bloge()
        a.heading=request.POST['heading']
        a.img=request.POST['ig']
        a.details=request.POST['det']
        a.save()

        return render(request,"bloge.html")
    return render(request,"bloge.html") 

def showBLOGE(request):
    d=bloge.objects.all()
    return render(request,"showbloge.html",{'rec':d})   



def reg(request):
    data=contectus.objects.all()
    return render(request,"aspage.html",{'myrecord':data}) 
            





