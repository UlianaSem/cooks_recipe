from django.views.generic import ListView
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Recipe, Product, ProductRecipe
from main.serializers import ProductRecipeSerializer, ProductSerializer
from main.services import cook_recipe


class AddProductAPIView(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter("recipe_id", OpenApiTypes.INT, OpenApiParameter.QUERY),
            OpenApiParameter("product_id", OpenApiTypes.INT, OpenApiParameter.QUERY),
            OpenApiParameter("weight", OpenApiTypes.INT, OpenApiParameter.QUERY),
        ],
        responses=ProductRecipeSerializer,
    )
    def get(self, request, format=None):
        recipe_id = self.request.query_params.get('recipe_id')
        product_id = self.request.query_params.get('product_id')
        weight = self.request.query_params.get('weight')

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        product_in_recipe, is_created = ProductRecipe.objects.update_or_create(
            product=product,
            recipe=recipe,
            defaults={"quantity": weight},
            create_defaults={"product": product, "recipe": recipe, "quantity": weight}
        )

        return Response(status=status.HTTP_200_OK, data=ProductRecipeSerializer(product_in_recipe).data)


class CookRecipeAPIView(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter("recipe_id", OpenApiTypes.INT, OpenApiParameter.QUERY),
        ],
        responses=ProductSerializer(many=True),
    )
    def get(self, request, format=None):
        recipe_id = self.request.query_params.get('recipe_id')
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        products = cook_recipe(recipe=recipe)

        return Response(status=status.HTTP_200_OK, data=ProductSerializer(products, many=True).data)


class ShowRecipesListView(ListView):
    model = Recipe

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.GET.get('product_id')

        queryset = (queryset.filter(products__id=product_id).filter(products_in_recipe__quantity__lt=10)
                    | queryset.exclude(products__id=product_id))

        return queryset
