from django.shortcuts import render, redirect
from .forms import EncryptionForm
from .models import EncryptedText

def encrypt_text(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            # Implement the encryption algorithm here
            encrypted_text = text
            EncryptedText.objects.create(text=text, encrypted_text=encrypted_text)
            return redirect('decrypt_text')
    else:
        form = EncryptionForm()
    return render(request, 'encrypt.html', {'form': form})

def decrypt_text(request):
    encrypted_texts = EncryptedText.objects.all()
    decrypted_texts = []
    for encrypted_text in encrypted_texts:
        # Implement the decryption algorithm here
        decrypted_text = encrypted_text.encrypted_text
        decrypted_texts.append(decrypted_text)
    return render(request, 'decrypt.html', {'decrypted_texts': decrypted_texts})
