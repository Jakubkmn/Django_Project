from time import time
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"""
        name = {self.name};
        quantity = {self.quantity};
        unit = {self.unit};
        price = {self.price}
        """
    
    def get_absolute_url(self):
        return "/ingredients"
class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return '/menu'

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def __str__(self):
        return f"name={self.name}; price={self.price}"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f'menu_item={self.menu_item}; ingredient={self.ingredient}; quantity={self.quantity}'
    
    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        return self.quantity <= self.ingredient.quantity
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}'

    def get_absolute_url(self):
        return '/purchases' 