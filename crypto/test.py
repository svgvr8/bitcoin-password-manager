import django
django.setup()
from django.test import TestCase
from crypto.forms import EncryptionForm, DecryptionForm

class EncryptionFormTestCase(TestCase):
    def test_form_has_fields(self):
        form = EncryptionForm()
        expected_fields = ['text']
        self.assertSequenceEqual(expected_fields, list(form.fields))

class DecryptionFormTestCase(TestCase):
    def test_form_has_fields(self):
        form = DecryptionForm()
        expected_fields = ['text']
        self.assertSequenceEqual(expected_fields, list(form.fields))
