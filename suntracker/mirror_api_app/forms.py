from django import forms

class MainOptions(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    height = forms.FloatField(label='Height: ')
    distance = forms.FloatField(label='Distance: ')
    latitude = forms.FloatField(label='Latitude: ')
    longitude = forms.FloatField(label='Longitude: ')
    direction = forms.FloatField(label='Direction: ')
    
