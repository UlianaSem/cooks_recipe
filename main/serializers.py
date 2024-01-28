from rest_framework.serializers import ModelSerializer

from main.models import ProductRecipe, Product


class ProductRecipeSerializer(ModelSerializer):

    class Meta:
        model = ProductRecipe
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
