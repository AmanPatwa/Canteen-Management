from django.shortcuts import render
from django import forms
from .models import Foodname


class FoodForm(forms.ModelForm):

    class Meta:
        model = Foodname
        fields = ('name', 'image')


    # def __init__(self):
    #     super().__init__(fields,*args,**kwargs)
