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



]




