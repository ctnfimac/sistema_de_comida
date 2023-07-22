from django import forms


class RegistroForm(forms.Form):
    TIPO_CHOICES = [('1', 'Cliente'),('2','Delivery'),('3','Comercio')]
    tipo = forms.ChoiceField(
        label = 'Tipo de Usuario',
        choices= TIPO_CHOICES,
        widget=forms.Select(
            attrs={
                'class':'browser-default custom-select mb-4'
            }
        )
    )
    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'ingrese su Email...'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'ingrese su Contraseña...'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'repita su Contraseña...'
            }
        )
    )

    telefono = forms.CharField(
        label='Teléfono',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'ingrese su teléfono...'
            }
        )
    )

    # class Media:
    #     js = ("js/web/forms/contactoForm.js",)

