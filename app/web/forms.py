from django import forms

#TODO: Agregar el campo para el checkbox
class LoginForm(forms.Form):
    usuario = forms.EmailField(
        label='Usuario', 
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-4', 
                    'placeholder': 'ingrese su usuario...'
                }
        ))
    contrasenia = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(
             attrs={'class': 'form-control mb-4',
                    'placeholder': 'ingrese su contraseña...'
                }
        ))
        


