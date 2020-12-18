from django.urls import path
from .views import *

app_name = "deposit"

urlpatterns = [
    path('', deposit, name="deposit"),
]
