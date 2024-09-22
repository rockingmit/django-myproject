from django.urls import path
from .views import get_restapi


urlpatterns = [
    path("get-country/", get_restapi.get_country),
    path("get-ex/", get_restapi.get_data)
]