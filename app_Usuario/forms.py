from django import forms
from .models import Usuario, Portafolio

class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'contrasena', 'saldo', 'activo', 'foto']
        widgets = {
            'contrasena': forms.PasswordInput(render_value=True),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class PortafolioForm(forms.ModelForm):
    class Meta:
        model = Portafolio
        fields = [ 'nombre_port', 'fecha', 'descripcion', 'valor_total']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }