from django import forms
from .models import Usuario, Registro, Cuarto, Departamento

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'contrasena']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellidos', 'email', 'usuario', 'contrasena']

class CuartoForm(forms.ModelForm):
    class Meta:
        model = Cuarto
        fields = ['direccion', 'fotos', 'caracteristicas', 'precio', 'disponible', 'usuario']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['direccion', 'fotos', 'caracteristicas', 'precio', 'disponible', 'usuario']
