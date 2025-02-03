from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
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

    class Meta:
        model = models.Contact
        fields = 'first_name','last_name','phone','email','description','category'