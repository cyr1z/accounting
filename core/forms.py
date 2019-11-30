from django import forms


class CardFilters(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()