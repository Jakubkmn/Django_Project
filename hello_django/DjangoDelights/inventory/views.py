from distutils.log import Log
from typing import List
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'


class IngredientView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'ingredient_delete.html'

class MenuView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'menu_view.html'

class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'purchase_view.html'

class Report(LoginRequiredMixin, TemplateView):
    template_name = 'report.html'