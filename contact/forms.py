from django import forms
from . import models

class ContactForm(forms.ModelForm):
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

    class Meta:
        model = models.Contact
        fields = 'first_name','last_name','phone',