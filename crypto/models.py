from django.db import models

class EncryptedText(models.Model):
    text = models.TextField()
    encrypted_text = models.TextField()
    
    def __str__(self):
        return self.text
