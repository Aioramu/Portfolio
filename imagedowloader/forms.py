from django import forms
from django.contrib.auth.models import User
from .models import Gallery
from django.utils.translation import ugettext, ugettext_lazy as _

g=[i.name for i in Gallery.objects.all()]
num=[x for x in range(len(g))]
Gallery=[]
for i in g:
    a=(i,i)
    Gallery.append(a)
#Gallery=[('1', 'First'), ('2', 'Second')]
class UploadFileForm(forms.Form):
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=Gallery)
    image = forms.ImageField()
