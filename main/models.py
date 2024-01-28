from django.db.models import Model, CharField, IntegerField, ForeignKey, ManyToManyField, CASCADE


class Product(Model):
    name = CharField(max_length=155, verbose_name="название")
    number_of_uses = IntegerField(default=0, verbose_name="количество использований")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class ProductRecipe(Model):
    product = ForeignKey(Product, verbose_name="продукт", on_delete=CASCADE)
    recipe = ForeignKey('Recipe', verbose_name="рецепт", on_delete=CASCADE)
    quantity = IntegerField(verbose_name="количество в г")

    def __str__(self):
        return f'{self.recipe.name}: {self.product.name}'

    class Meta:
        verbose_name = "продукт в рецепте"
        verbose_name_plural = "продукты в рецепте"
        unique_together = ['product', 'recipe']


class Recipe(Model):
    name = CharField(max_length=155, verbose_name="название")
    products = ManyToManyField(
        Product, through='ProductRecipe', through_fields=('recipe', 'product'), verbose_name="продукты"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "рецепт"
        verbose_name_plural = "рецепты"
