from django.test import TestCase
from .forms import EncryptionForm, DecryptionForm

class EncryptionDecryptionTestCase(TestCase):

    def test_encryption_form(self):
        form_data = {'text': 'test text'}
        form = EncryptionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_decryption_form(self):
        form_data = {'encrypted_text': 'test text'}
        form = DecryptionForm(data=form_data)
        self.assertTrue(form.is_valid())
