from django.urls import path
from .views import *

app_name = "withdraw"

urlpatterns = [
    path('', withdraw, name="withdraw"),
]
