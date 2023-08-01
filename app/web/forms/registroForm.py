from django import forms
from django.contrib.auth.hashers import make_password
from web.models.usuario import Usuario


class RegistroForm(forms.ModelForm):

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
    
    class Meta:
        model = Usuario
        fields = ['tipo', 'email', 'telefono','contrasenia']

    
    class Media:
        js = ('js/web/forms/registroForm.js',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tipo"].widget.attrs.update({"class": "browser-default custom-select mb-4"})
        self.fields["email"].widget.attrs.update({
            "class": "form-control form-control-sm",
            'placeholder': 'ingrese su Email...'
        })
        self.fields["telefono"].widget.attrs.update({
            "class": "form-control form-control-sm",
            'placeholder': 'ingrese su teléfono...'
        })
        self.fields["contrasenia"].widget.attrs.update({
            "class": "form-control form-control-sm",
            'placeholder': 'ingrese su Contraseña...'
        })
        
    def save(self, commit=True):
        instance = super().save(commit=False)

        obj = Usuario.objects.create(
            email=instance.email, 
            contrasenia=make_password(instance.contrasenia), 
            telefono=instance.telefono, 
            tipo=instance.tipo 
        )
        
        if commit:
            obj.save()
        return obj

    def clean_contrasenia(self):
        if self.cleaned_data['contrasenia'] != self['password2'].value():
            self.add_error('password2', 'Las contraseñas no son iguales.')
        return self.cleaned_data['contrasenia']
    