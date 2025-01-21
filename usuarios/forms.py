from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            'invalid': 'Digite um endereço de e-mail válido.',
            'required': 'O campo de e-mail é obrigatório.'
        }
    )
    
    is_superuser = forms.ChoiceField(
        choices=[(False, 'Usuário comum'), (True, 'Superusuário')],
        widget=forms.Select(attrs={'class': 'select-custom'}),
        required=True,
        label="Tipo de Conta"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']
        error_messages = {
            'username': {
                'required': 'O nome de usuário é obrigatório.',
                'unique': 'Este nome de usuário já está em uso.',
                'invalid': 'Digite um nome de usuário válido.',
                'max_length': 'O nome de usuário deve ter no máximo 150 caracteres.'
            },
            'password2': {
                'required': 'A confirmação da senha é obrigatória.',
                'password_mismatch': 'As senhas não coincidem.'
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso. Tente outro.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        try:
            validate_password(password)
        except ValidationError as e:
            raise ValidationError([
                erro.replace("This password", "A senha").replace("too common", "muito comum")
                .replace("too short", "muito curta (mínimo de 8 caracteres)")
                .replace("entirely numeric", "não pode ser composta apenas por números")
                for erro in e.messages
            ])
        return password
