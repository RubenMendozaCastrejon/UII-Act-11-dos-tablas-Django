from django import forms
from .models import Usuario, Portafolio

class UsuarioForm(forms.ModelForm):
    # Opcionalmente, puedes añadir validaciones personalizadas o widgets aquí
    # Por ejemplo, para el campo de contraseña, es común no pedirlo en un ModelForm
    # si se va a hashear, o usar PasswordInput para ocultar la entrada.
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = Usuario
        # Excluir 'fecha_registro' ya que se auto_now_add
        # Excluir 'saldo_cuenta' y 'moneda' si se establecen con valores por defecto o en lógica de negocio
        fields = ['nombre', 'apellido', 'email', 'contrasena', 'foto_perfil']
        # Si prefieres una lista de exclusión en lugar de inclusión
        # exclude = ['fecha_registro', 'saldo_cuenta', 'moneda']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            # 'contrasena': forms.PasswordInput(), # Ya lo estamos haciendo con el campo definido arriba
        }

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            self.add_error('confirmar_contrasena', "Las contraseñas no coinciden.")

        return cleaned_data

class PortafolioForm(forms.ModelForm):
    class Meta:
        model = Portafolio
        # Excluir 'usuario' ya que probablemente se asignará en la vista
        # Excluir 'fecha' y 'valor_total' si se auto_now_add o se calculan
        fields = ['nombre', 'descripcion']
        # Si prefieres una lista de exclusión
        # exclude = ['usuario', 'fecha', 'valor_total']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }