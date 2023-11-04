from django.shortcuts import render
from carsapp.forms import car_form

# Create your views here.
def car_form_view(request):
    form = car_form()

    if request.method == "POST":

        form = car_form(request.POST)

        if form.is_valid():
            form.save()


    return render(request, 'car.html',{'form':form})
