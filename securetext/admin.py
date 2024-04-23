from django.contrib import admin
from .models import EncryptedMessage
from .models import SecureTextURL
from .models import DecryptKey

admin.site.register(EncryptedMessage)
admin.site.register(SecureTextURL)
admin.site.register(DecryptKey)