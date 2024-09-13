from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_desc = models.TextField()
    food_img = models.ImageField()
