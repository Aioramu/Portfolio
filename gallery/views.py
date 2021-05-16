from django.shortcuts import render
from imagedowloader.models import Image,Gallery


# Create your views here.
def index(request):
    return render(request,"base.html")

def gallery(request):
    i=Image.objects.all()
    b=[]
    for j in i:
        b.append('static/media/'+str(j.path))
    print(b)
    return render(request,"images.html",{'b':b})
