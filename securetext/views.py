from django.views.generic import TemplateView
from django.views.generic import CreateView
from .models import EncryptedMessage

class SecureMessageView(CreateView):
    model = EncryptedMessage
    template_name = 'securemessage.html'
    fields = ['encrypted_text']
