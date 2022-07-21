from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('ingredients/new', views.AddIngredientView.as_view(), name='add_ingredient'),
    path('ingredients/<slug:pk>/update', views.UpdateIngredientView.as_view(), name='ingredient_update'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/new', views.NewMenuView.as_view(), name='add_menu'),
    path('reciperequirement/new', views.NewRecipeView.as_view(), name="add_recipe"),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path('purchase/new', views.NewPurchaseView.as_view(), name='add_purchase'),
    path('reports', views.ReportView.as_view(), name='reports')
]