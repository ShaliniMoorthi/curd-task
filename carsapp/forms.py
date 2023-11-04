from django import forms
from carsapp.models import cars

class car_form(forms.ModelForm):
    class Meta:
        model = cars
        fields = '__all__'