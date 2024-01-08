from django import forms
from app.models import *

#creating a forms

class Topicform(forms.ModelForm):
    class Meta():
        model = Topic
        fields = '__all__'
        #labels = {'topic_name':'TN'} #used to change the name of the colmun


        

class Webpageform(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'
        #widgets = {'email':forms.PasswordInput()} #used to change the type of fields by our requriment

class Acessrecordform(forms.ModelForm):
    class Meta():
        model = Acessrecord
        fields = '__all__'
        #fields = ['name','author'] #used to mention specified inputs from forms
        #exclude = ['number'] #used to avoid specified input from forms
        

        