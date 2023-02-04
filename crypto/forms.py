from django import forms

class EncryptionForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
