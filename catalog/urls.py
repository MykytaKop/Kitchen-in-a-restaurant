from django.urls import path


from catalog.views import (
    index,
    CookListView,
    CookCreateView,
    CookDetailView,
    CookDeleteView,
    CookUpdateView,
    DishListView,
    DishCreateView,
    DishDetailView,
    DishDeleteView,
    DishUpdateView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    toggle_assign_to_dish,
    IngredientsListView,
    IngredientsUpdateView,
    IngredientsDeleteView,

)

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish_type_list/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish_type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path(
        "diahes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
    path("ingredients/", IngredientsListView.as_view(), name="ingredient-list"),
    path("ingredients/<int:pk>", IngredientsUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete", IngredientsDeleteView.as_view(), name="ingredient-delete"),


]




