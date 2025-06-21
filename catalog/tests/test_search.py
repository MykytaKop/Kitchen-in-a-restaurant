from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from catalog.models import Cook, Dish, DishType, Ingredient


class SearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test user",
            password="testPassword123",
            years_of_experience="2"
        )
        self.client.force_login(self.user)

        self.dishtype = DishType.objects.create(
            name="TestDishType",
        )
        self.ingredients = Ingredient.objects.create(
            name="Test Ingredient",
        )
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test Dish Description",
            dish_type=self.dishtype,
            price=100,


        )
        self.dish.ingredients.set([self.ingredients])
        self.dish.cooks.add(self.user)

    def test_search_driver(self):
        response = self.client.get(
            reverse("catalog:cook-list"),
            {"username": "test user"}
        )
        self.assertContains(response, "test user")

    def test_search_dish_type(self):
        response = self.client.get(
            reverse("catalog:dish-type-list"),
            {"dish type": "TestDishType"}
        )
        self.assertContains(response, "TestDishType")

    def test_search_car(self):
        response = self.client.get(
            reverse("catalog:dish-list"),
            {"name": "Test dish"})
        self.assertContains(response, "Test dish")
