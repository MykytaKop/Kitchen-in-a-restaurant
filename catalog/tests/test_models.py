from django.test import TestCase
from catalog.models import Cook, Dish, DishType, Ingredient
from catalog.forms import *


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="testName"
        )
        self.assertEqual(
            str(dish_type), f"{dish_type.name}"
        )

    def test_cook_str(self):
        cook = Cook.objects.create(
            username="testusername",
            first_name="testfirst",
            last_name="testlast",
            years_of_experience=3
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name}, years_of_experience: {cook.years_of_experience})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="testName"
        )
        dish = Dish.objects.create(
            name="testName",
            price=10,
            dish_type_id=dish_type.id,

        )
        self.assertEqual(str(dish), f"{dish.name}")
