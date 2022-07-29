from django.urls import path
from .views import home, delete, update


urlpatterns = [
    path('', home, name="home"),
    path('delete', delete, name="delete_data"),
    path('t/<id>/', update, name="update"),
]
