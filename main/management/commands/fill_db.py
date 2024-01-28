from django.core.management import BaseCommand

from main.models import Product, Recipe, ProductRecipe


class Command(BaseCommand):

    products = ['Творог', 'Яйцо', 'Сахар', 'Куриное филе']
    recipes = ['Сырник', 'Яичница']

    def handle(self, *args, **options):

        product_1 = Product.objects.create(name=self.products[0])
        product_2 = Product.objects.create(name=self.products[1])
        product_3 = Product.objects.create(name=self.products[2])
        product_4 = Product.objects.create(name=self.products[3])

        recipe_1 = Recipe.objects.create(name=self.recipes[0])
        recipe_2 = Recipe.objects.create(name=self.recipes[1])

        ProductRecipe.objects.create(recipe=recipe_1, product=product_1, quantity=200)
        ProductRecipe.objects.create(recipe=recipe_1, product=product_2, quantity=50)
        ProductRecipe.objects.create(recipe=recipe_1, product=product_3, quantity=10)

        ProductRecipe.objects.create(recipe=recipe_2, product=product_2, quantity=50)
