from distutils.log import Log
from django.db.models import Sum
from multiprocessing import context
from typing import List
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'temp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['purchase'] = Purchase.objects.all()  
        return context

class IngredientView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'temp/ingredients_list.html'


class AddIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'temp/add_ingredient.html'
class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'temp/ingredient_update.html'
    form_class = IngredientForm

class MenuView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'temp/menu_view.html'

class NewMenuView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'temp/add_menu.html'

class NewRecipeView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class  = RecipeForm
    template_name = 'temp/add_recipe.html'

class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'temp/purchase_view.html'

class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = 'temp/add_purchase.html'

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = 'temp/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase'] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue=Sum('menu_item__price'))['revenue']
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price * recipe_requirement.quantity
        
        context['revenue'] = revenue
        context['total_cost'] = total_cost
        context['profit'] = revenue - total_cost
        return context
def log_out(request):
    logout(request)
    return redirect('/')