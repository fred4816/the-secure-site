from django.db import models
from django.urls import reverse

class EncryptedMessage(models.Model):
    encrypted_text = models.TextField()

    def get_absolute_url(self):
        return reverse('securemessage')


class SecureTextURL(models.Model):
    url = models.TextField()
    encrypted_text = models.ForeignKey('EncryptedMessage', on_delete=models.CASCADE)
    decrypte_key = models.ForeignKey('DecryptKey', on_delete=models.CASCADE)


class DecryptKey(models.Model):
    decrypt_key = models.TextField()
