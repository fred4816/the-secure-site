from django.urls import path
from .views import PasswordGeneratorView

urlpatterns = [
    path('passwordgenerator', PasswordGeneratorView.as_view(), name='passwordgenerator')
]