# Generated by Django 5.0.1 on 2024-01-28 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='название')),
                ('number_of_uses', models.IntegerField(default=0, verbose_name='количество использований')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='количество в г')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'продукт в рецепте',
                'verbose_name_plural': 'продукты в рецепте',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='название')),
                ('products', models.ManyToManyField(through='main.ProductRecipe', to='main.product', verbose_name='продукты')),
            ],
            options={
                'verbose_name': 'рецепт',
                'verbose_name_plural': 'рецепты',
            },
        ),
        migrations.AddField(
            model_name='productrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recipe', verbose_name='рецепт'),
        ),
        migrations.AlterUniqueTogether(
            name='productrecipe',
            unique_together={('product', 'recipe')},
        ),
    ]
