from django.db import models

class Usuario(models.Model):
    # El id_usuario se gestiona automáticamente por Django como la llave primaria por defecto (id)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True) # Se establece automáticamente al crear el usuario
    saldo_cuenta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    moneda = models.CharField(max_length=3, default='USD')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Portafolio(models.Model):
    # El id_portafolio se gestiona automáticamente por Django como la llave primaria por defecto (id)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='portafolio')
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True) # Se establece automáticamente al crear el portafolio
    descripcion = models.TextField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Portafolio de {self.usuario.nombre} - {self.nombre}"

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"