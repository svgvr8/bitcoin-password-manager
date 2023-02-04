from django.shortcuts import render, redirect
from .forms import EncryptionForm
from .models import EncryptedText

# def encrypt_text(request):
#     if request.method == 'POST':
#         form = EncryptionForm(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             # Implement the encryption algorithm here
#             encrypted_text = text
#             EncryptedText.objects.create(text=text, encrypted_text=encrypted_text)
#             return redirect('decrypt_text')
#     else:
#         form = EncryptionForm()
#     return render(request, 'encrypt.html', {'form': form})

# def decrypt_text(request):
#     encrypted_texts = EncryptedText.objects.all()
#     decrypted_texts = []
#     for encrypted_text in encrypted_texts:
#         # Implement the decryption algorithm here
#         decrypted_text = encrypted_text.encrypted_text
#         decrypted_texts.append(decrypted_text)
#     return render(request, 'decrypt.html', {'decrypted_texts': decrypted_texts})

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            if char.islower():
                encrypted_text += shift_char.lower()
            else:
                encrypted_text += shift_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 90 - shift) % 26 + 90)
            if char.islower():
                text += shift_char.lower()
            else:
                text += shift_char
        else:
            text += char
    return text


def encrypt_text(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            shift = form.cleaned_data['shift']
            encrypted_text = encrypt(text, shift)
            EncryptedText.objects.create(text=text, encrypted_text=encrypted_text)
            return redirect('decrypt_text')
    else:
        form = EncryptionForm()
    return render(request, 'templates/crypto/encrypt.html', {'form': form})

def decrypt_text(request):
    encrypted_texts = EncryptedText.objects.all()
    decrypted_texts = []
    for encrypted_text in encrypted_texts:
        decrypted_text = decrypt(encrypted_text.encrypted_text, shift)
        decrypted_texts.append(decrypted_text)
    return render(request, 'templates/crypto/decrypt.html', {'decrypted_texts': decrypted_texts})
