from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text="Nombre del usuario")
    apellido = models.CharField(max_length=100, help_text="Apellido del usuario")
    email = models.EmailField(max_length=255, help_text="Correo electrónico del usuario")
    contrasena = models.CharField(max_length=255, help_text="Contraseña del usuario")
    saldo = models.DecimalField(max_digits=15, decimal_places=2, help_text="Saldo disponible del usuario")
    activo = models.BooleanField(default=True, help_text="Indica si el usuario está activo")
    foto = models.ImageField(upload_to='img_usuarios/', blank=True, null=True, help_text="Foto de perfil del usuario")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Portafolio(models.Model):
    id_portafolio = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='portafolios')
    nombre_port = models.CharField(max_length=100, help_text="Nombre del portafolio")
    fecha = models.DateField(help_text="Fecha de creación del portafolio")
    descripcion = models.TextField(help_text="Descripción del portafolio")
    valor_total = models.DecimalField(max_digits=15, decimal_places=2, help_text="Valor total del portafolio")

    def __str__(self):
        return f"{self.nombre_port} - {self.id_usuario.nombre}"

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"