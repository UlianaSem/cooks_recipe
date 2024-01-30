from django.db.models import F

from main.models import Recipe


def cook_recipe(recipe: Recipe):
    """
    Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.
    :param recipe: объект типа Recipe
    :return: QuerySet объектов типа Product
    """
    products = recipe.products.all()

    for product in products:
        product.number_of_uses = F('number_of_uses') + 1
        product.save()
        product.refresh_from_db()

    return products
