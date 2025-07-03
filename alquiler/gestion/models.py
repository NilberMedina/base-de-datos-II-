from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Registro(models.Model):
    id = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Cuarto(models.Model):
    direccion = models.CharField(max_length=200)
    fotos = models.TextField()
    caracteristicas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Departamento(models.Model):
    direccion = models.CharField(max_length=200)
    fotos = models.TextField()
    caracteristicas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)