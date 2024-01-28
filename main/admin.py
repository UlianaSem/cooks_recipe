from django.contrib import admin

from main.models import Product, ProductRecipe, Recipe


admin.site.register(Product)


class ProductRecipeInline(admin.TabularInline):
    model = ProductRecipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductRecipeInline]
