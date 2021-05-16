from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .models import Image,Gallery
from django.core.mail import send_mail

User = get_user_model()
# Create your views here.
def index(request):
    return render(request,"imagedowloader/base.html")

def logout_view(request):
    logout(request)
    return redirect('index')
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST['choice_field'])
            gallery=Gallery.objects.get(name=request.POST['choice_field'])
            instance = Image(gallery=gallery,path=request.FILES['image'])
            instance.save()

            return render(request,"imagedowloader/base.html")
    else:
        form = UploadFileForm()
    return render(request, 'imagedowloader/upload.html', {'form': form})
@login_required
def lk(request):
    img=ImageList.objects.filter(user=request.user)
    s=img.order_by('-pub_date')
    if request.method!='POST':
        form = UploadFileForm()
        #hist=img.get_path_history()
        return render(request,"imagedowloader/list.html",{'form': form,'img':s,})
    else:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['image'])
            instance=ImageList.objects.get(pk=request.POST['id'])
            instance.path=request.FILES['image']
            instance.save()
            #ins=request.data.id
        return render(request,"list.html",{'form': form,'img':s})
