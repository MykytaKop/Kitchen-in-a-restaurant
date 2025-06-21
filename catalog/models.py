from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"


    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name}, years_of_experience: {self.years_of_experience})"

    def get_absolute_url(self):
        return reverse("catalog:cook-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    dish_type = models.ForeignKey(DishType,
                                  on_delete=models.CASCADE,
                                  related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    def __str__(self):
        return self.name
