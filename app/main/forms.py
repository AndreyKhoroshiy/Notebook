from .models import Contacts
from django.forms import ModelForm, TextInput, Textarea


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name',
                  'preview',
                  'country',
                  'town',
                  'organization',
                  'telephone',
                  'email'
                  ]

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'preview': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткая информация'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            'town': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'organization': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Организация'
            }),
            'telephone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта'
            })
        }
