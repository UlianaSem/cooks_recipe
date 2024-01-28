from django.urls import path

from main.apps import MainConfig
from main.views import AddProductAPIView, CookRecipeAPIView, ShowRecipesListView

app_name = MainConfig.name


urlpatterns = [
    path('add_product_to_recipe/', AddProductAPIView.as_view(), name='add_product'),
    path('cook_recipe/', CookRecipeAPIView.as_view(), name='cook_recipe'),
    path('show_recipes_without_product/', ShowRecipesListView.as_view(), name='show_recipes'),
]
