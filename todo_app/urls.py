# todo_app/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, create_todo, todo_list

app_name = 'todos'  # This is the namespace
router = DefaultRouter()
router.register("", TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("create/", create_todo, name="create"),
    path("list", todo_list, name="todo_list"),
]