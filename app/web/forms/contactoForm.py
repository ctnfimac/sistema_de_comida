from django import forms

class ContactoForm(forms.Form):
    MOTIVO_CHOICES = [('1', 'Feedback'),('2','Reportar mal servicio')]
    nombre = forms.CharField(
        label='Nombre',
        max_length='30',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
            'placeholder': 'ingrese su Nombre..'
            }
        ))
    
    email = forms.CharField(
        label='Email',
        max_length='50',
        widget= forms.TextInput(
            attrs={'class': 'form-control',
            'placeholder': 'ingrese su Email..'
            }
        ))
    
    subject = forms.ChoiceField(
        label='Motivo',
        choices=MOTIVO_CHOICES, 
        widget = forms.Select(
            attrs={
                'class':'form-control rounded-0',
            }
        )  
    )

    mensaje = forms.CharField(
        widget = forms.Textarea
       (
            attrs={
                'class':'form-control rounded-0',
                'placeholder': 'escriba su mensaje...',
                'rows':4, 
                'cols':15
            }
        )
    )

    copia = forms.BooleanField(
        label = 'Enviarme copia',
        widget= forms.CheckboxInput(
             attrs={
                'class':'form-check-input',
            }
        ))