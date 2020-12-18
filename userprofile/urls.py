from django.urls import path
from .views import *

app_name = "profile"

urlpatterns = [
    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('change-password', change_password, name='change-password'),
]
