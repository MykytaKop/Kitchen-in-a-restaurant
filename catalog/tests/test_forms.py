from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.forms import CookCreationForm, CookUpdateForm


class TestForms(TestCase):
    def test_cook_creation_form(self):
        form_data = {
            "username": "Test",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "TestFirst",
            "last_name": "TestLast",
            "years_of_experience": 2,
            "email": "testemail@test.com",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_update_form(self):
        user = get_user_model().objects.create_user(
            username="testUser",
            password="test12345",
            years_of_experience=1,
            email="old@test.com"
        )
        form_data = {
            "username": "testUser",
            "first_name": "UpdatedFirst",
            "last_name": "UpdatedLast",
            "years_of_experience": 5,
            "email": "test@test.com",
        }
        form = CookUpdateForm(data=form_data, instance=user)
        print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["years_of_experience"], 5)
        self.assertEqual(form.cleaned_data["email"], "test@test.com")
