from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("new_page/", views.new_page, name="new_page"),
    path("random_pg/", views.random_page, name="random_pg"),
    path("<str:title>/", views.titles, name="titles"),
    ]
