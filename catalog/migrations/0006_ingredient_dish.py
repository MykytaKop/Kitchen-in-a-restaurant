# Generated by Django 5.2.2 on 2025-06-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_ingredient_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='dish',
            field=models.ManyToManyField(related_name='ingredients', to='catalog.dish'),
        ),
    ]
