from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def food(request):
    if request.method == "POST":
       data = request.POST

       food_img = request.FILES.get("food_img")
       food_name = data.get("food_name")
       food_desc = data.get("food_desc")
       

       print(food_img)
       print(food_name)
       print(food_desc)

       Food.objects.create(
           food_img = food_img,
           food_name = food_name,
           food_desc = food_desc

       )

       return redirect('/food/')
    return render(request, 'food.html')
