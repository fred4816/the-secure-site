from django.urls import path
from .views import SecureMessageView

urlpatterns = [
    path('securemessage', SecureMessageView.as_view(), name='securemessage')
]