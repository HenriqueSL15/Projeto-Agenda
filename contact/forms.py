from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from . import models

class RegisterForm(UserCreationForm):
    ...

class ContactForm(forms.ModelForm):


    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = 'first_name','last_name','phone','email','description','category', 'picture',

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError("O último nome não pode ser igual ao primeiro nome", code='invalid')
            self.add_error('last_name',msg)
    

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text="Texto de ajuda para seu usuário"
    )