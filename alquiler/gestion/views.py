from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Registro, Cuarto, Departamento
from .forms import UsuarioForm, RegistroForm, CuartoForm, DepartamentoForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'gestion/lista_usuarios.html', {'usuarios': usuarios})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')

def lista_registros(request):
    registros = Registro.objects.select_related('id').all()
    return render(request, 'gestion/lista_registros.html', {'registros': registros})

def agregar_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario.objects.create(
                usuario=form.cleaned_data['usuario'],
                contrasena=form.cleaned_data['contrasena']
            )
            Registro.objects.create(
                id=nuevo_usuario,
                nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'],
                email=form.cleaned_data['email'],
                usuario=form.cleaned_data['usuario'],
                contrasena=form.cleaned_data['contrasena']
            )
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'gestion/agregar_registro.html', {'form': form})

def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            registro.id.usuario = form.cleaned_data['usuario']
            registro.id.contrasena = form.cleaned_data['contrasena']
            registro.id.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'gestion/editar_registro.html', {'form': form})

def eliminar_registro(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_registros')


def lista_cuartos(request):
    cuartos = Cuarto.objects.select_related('usuario').all()
    return render(request, 'gestion/lista_cuartos.html', {'cuartos': cuartos})

def agregar_cuarto(request):
    if request.method == 'POST':
        form = CuartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cuartos')
    else:
        form = CuartoForm()
    return render(request, 'gestion/agregar_cuarto.html', {'form': form})

def editar_cuarto(request, pk):
    cuarto = get_object_or_404(Cuarto, pk=pk)
    if request.method == 'POST':
        form = CuartoForm(request.POST, instance=cuarto)
        if form.is_valid():
            form.save()
            return redirect('lista_cuartos')
    else:
        form = CuartoForm(instance=cuarto)
    return render(request, 'gestion/editar_cuarto.html', {'form': form})

def eliminar_cuarto(request, pk):
    cuarto = get_object_or_404(Cuarto, pk=pk)
    cuarto.delete()
    return redirect('lista_cuartos')

def lista_departamentos(request):
    departamentos = Departamento.objects.select_related('usuario').all()
    return render(request, 'gestion/lista_departamentos.html', {'departamentos': departamentos})

def agregar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'gestion/agregar_departamento.html', {'form': form})

def editar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('lista_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'gestion/editar_departamento.html', {'form': form})

def eliminar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    departamento.delete()
    return redirect('lista_departamentos')