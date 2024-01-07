from django import forms
from app.models import *

#creating a forms

class Topicform(forms.ModelForm):
    class Meta():
        model = Topic
        fields = '__all__'

class Webpageform(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'

class Acessrecordform(forms.ModelForm):
    class Meta():
        model = Acessrecord
        fields = '__all__'

        