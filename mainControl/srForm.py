from django import forms
from mainControl import models

class sRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Students
        fields = "__all__"

class sInformationForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Students_Information
        fields = '__all__'